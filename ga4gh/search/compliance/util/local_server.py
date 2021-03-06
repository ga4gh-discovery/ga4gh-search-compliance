# -*- coding: utf-8 -*-
"""Module compliance_suite.report_server.py

This module contains class definition of small web server utility. Serves final
report results as HTML.
"""

import datetime
import time
import http.server
import socketserver
import os
import logging
import inspect
import socket
import webbrowser
import shutil
import sys
import threading
import json
import jinja2 as j2
import ga4gh.search.compliance as pkg_dir
from ga4gh.search.compliance.config.configuration import Configuration

def capitalize(text):
    """capitalizes a word, for use in rendering template

    Args:
        text (str): word to capitalize
    
    Returns:
        capitalized (str): capitalized word
    """

    return text[0].upper() + text[1:]

def get_route_status(route_obj):

    count_d = {
        "incomplete": 0,
        "pass": 0,
        "fail": 0,
        "warn": 0,
        "skip": 0
    }
    symbol_d = {
        "0": "incomplete",
        "1": "pass",
        "2": "warn",
        "3": "fail",
        "4": "skip",
        
    }
    ret = {
        "btn": "btn-danger",
        "text": "No Tests Run"
    }

    for test_case_report in route_obj["test_case_reports"]:
        count_d[symbol_d[str(test_case_report["status"])]] += 1

    if count_d["fail"] > 0 or count_d["skip"] > 0:
        ret = {
            "btn": "btn-danger",
            "text": "%s Failed / %s Skipped" % (str(count_d["fail"]),
                                                str(count_d["skip"]))
        }
    
    if count_d["pass"] > 0:
        ret = {
            "btn": "btn-success",
            "text": "Pass"
        }
    
    return ret


class LocalServer(object):
    """Creates web server, serves test report as HTML

    The ReportServer spins up a small, local web server to host test result
    reports once the final JSON object has been generated. The server can be
    shut down with CTRL+C.

    Attributes:
        port (Port): object representing free port to serve content
        httpd (TCPServer): handle for web server
        thread (Thread): thread serves content indefinitely, can be killed
            safely from the outside via CTRL+C
        web_dir (str): directory which host web files (CSS and generated HTML)
        cwd (str): working directory to change back to after creating server
        render_helper (dict): contains data structures and functions to be
            passed to rendering engine to aid in rendering HTML
    """

    def __init__(self):
        """instantiates a ReportServer object"""

        self.port = None
        self.httpd = None
        self.thread = None
        self.web_dir = Configuration.get_instance().get_output_dir()
        self.web_resource_dir = os.path.join(
            os.path.dirname(pkg_dir.__file__),
            "web"
        )

        self.cwd = os.getcwd()
        self.render_helper = {
            "s": { # s: structures
                "endpoints": [
                    "service_info",
                    "tables",
                    "table_info",
                    "table_data",
                    "search"
                ],
                "formatted": {
                    "service_info": "Service Info",
                    "tables": "Tables",
                    "table_info": "Table Info",
                    "table_data": "Table Data",
                    "search": "Search"
                },
                "status": {
                    0: {
                        "status": "INCOMPLETE",
                        "css_class": "text-danger",
                        "fa_class": "fa-times-circle"
                    },
                    1: {
                        "status": "PASS",
                        "css_class": "text-success",
                        "fa_class": "fa-check-circle"
                    },
                    2: {
                        "status": "WARN",
                        "css_class": "text-danger",
                        "fa_class": "fa-times-circle"
                    },
                    3: {
                        "status": "FAIL",
                        "css_class": "text-danger",
                        "fa_class": "fa-times-circle"
                    },
                    4: {
                        "status": "SKIP",
                        "css_class": "text-info",
                        "fa_class": "fa-ban"
                    }
                }
            },
            "f": { # f: functions
                "capitalize": capitalize,
                "format_test_name": lambda text: " ".join(
                    [capitalize(t) for t in text.split("_")]
                ),
                "server_name_url": lambda name: \
                    name.lower().replace(" ", "") + ".html",
                "rm_space": lambda text: text.replace(" ", "_")\
                                             .replace(",", ""),
                "timestamp": lambda: \
                    datetime.datetime.now(datetime.timezone.utc)\
                                     .strftime("%B %d, %Y at %l:%M %p (%Z)"),
                "route_status": get_route_status
            }
        }
    
    def setup(self):
        self.__set_free_port()
        self.__copy_web_resource_dir()
        self.__render_html()
    
    def serve(self, uptime=3600):
        """serves server as separate thread so it can be stopped from outside
        
        Args:
            uptime (int): server will remain up for this time in seconds unless
                shutdown by user
        """

        try:
            self.thread = threading.Thread(target=self.__start_mock_server,
                                        args=(uptime,))
            self.thread.start()
            time.sleep(uptime)
        except KeyboardInterrupt as e:
            print("stopping server")
        finally:
            self.httpd.shutdown()
            os.chdir(self.cwd)

    def __set_free_port(self):
        """get free port on local machine on which to run the report server

        This function is used in conftest and the return of this is a free port 
        available in the system on which the mock server will be run. This port
        will be passed to start_mock_server as a required parameter from 
        conftest.py

        Returns:
            (Port): free port on which to run server
        """

        s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
        s.bind(('localhost', 0))
        address, port = s.getsockname()
        s.close()
        self.port = port
    
    def __copy_web_resource_dir(self):
        for subdir in ["public"]:
            src = os.path.join(self.web_resource_dir, subdir)
            dst = os.path.join(self.web_dir, subdir)
            shutil.copytree(src, dst)
        

    def __render_html(self):
        
        data = None
        with open(self.web_dir + "/ga4gh-search-compliance-report.json", "r") as f:
            data = json.load(f)

        # set up jinja2 rendering engine
        view_loader = j2.FileSystemLoader(searchpath=self.web_resource_dir)
        view_env = j2.Environment(loader=view_loader)

        # render the index/homepage
        home_template = view_env.get_template("views/home.html")
        home_rendered = home_template.render(data=data, h=self.render_helper)
        home_path = self.web_dir + "/index.html"
        open(home_path, "w").write(home_rendered)

        for server_report in data["server_reports"]:
            report_template = view_env.get_template("views/report.html")
            report_rendered = report_template.render(server_report=server_report,
                                                     h=self.render_helper)
            report_path = self.web_dir + "/" + \
                self.render_helper["f"]["server_name_url"](server_report["name"])
            open(report_path, "w").write(report_rendered)
        
    def __start_mock_server(self, uptime):
        """run server to serve final test report

        Args:
            port (Port): port on which to run the server
        """

        os.chdir(self.web_dir)
        Handler = http.server.SimpleHTTPRequestHandler
        self.httpd = socketserver.TCPServer(("", self.port), Handler)
        logging.info("serving at http://localhost:" + str(self.port))
        webbrowser.open("http://localhost:" + str(self.port))
        logging.info("server will shut down after " + str(uptime) + " seconds, "
                     + "press CTRL+C to shut down manually")
        self.httpd.serve_forever()
