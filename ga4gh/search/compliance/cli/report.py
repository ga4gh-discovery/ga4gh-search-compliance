import json
import os
import shutil
import sys
from ga4gh.search.compliance.config.configuration import Configuration
from ga4gh.search.compliance.report.run_report import RunReport
from ga4gh.search.compliance.report.server_report import ServerReport
from ga4gh.search.compliance.tests import ALL_TEST_GROUP_CLS
from ga4gh.search.compliance.util.time_utils import TimeUtils

def report_handler(kwargs):

    def setup_configuration():
        Configuration.load_instance(kwargs)
        return Configuration.get_instance()
    
    def setup_run_report():
        RunReport.load_instance()
        run_report = RunReport.get_instance()
        run_report.set_started(TimeUtils.get_timestamp())
        return run_report

    def setup_output_directory(configuration):
        output_dir = configuration.get_output_dir()
        force = configuration.get_force()

        if os.path.exists(output_dir):
            if force:
                shutil.rmtree(output_dir)
                os.makedirs(output_dir)
            else:
                raise Exception("Output directory %s already exists" % output_dir)
        else:
            os.makedirs(output_dir)
    
    def execute_server_tests(server_config, server_report):
        
        for test_group_cls in ALL_TEST_GROUP_CLS:
            test_group_instance = test_group_cls(server_config)
            test_group_report = test_group_instance.execute_test_group()
            server_report.add_test_group_report(test_group_report)
    
    def finalize_run_report(run_report):
        run_report.set_finished(TimeUtils.get_timestamp())
    
    def write_run_report(configuration, run_report):
        report_file = os.path.join(configuration.get_output_dir(), "ga4gh-search-compliance-report.json")
        report_fh = open(report_file, "w")
        json_str = run_report.to_json()
        report_fh.write(json_str)
        report_fh.close()

    def handle():
        try:

            # initial setup
            configuration = setup_configuration()
            run_report = setup_run_report()
            setup_output_directory(configuration)

            # body of test suite, run all tests for all servers
            for server_config in configuration.get_run_config().get_servers():
                server_report = ServerReport()
                server_report.set_name(server_config.get_name())
                server_report.set_url(server_config.get_url())
                execute_server_tests(server_config, server_report)
                run_report.add_server_report(server_report)

            # finalize run report object and write to report file
            finalize_run_report(run_report)
            write_run_report(configuration, run_report)

        except Exception as e:
            print("exiting program: " + str(e))
            sys.exit(1)
    
    handle()
