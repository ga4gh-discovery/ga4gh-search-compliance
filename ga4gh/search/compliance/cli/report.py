import os
import sys
from ga4gh.search.compliance.config.configuration import Configuration
from ga4gh.search.compliance.report.run_report import RunReport
from ga4gh.search.compliance.util.time_utils import TimeUtils

def report_handler(kwargs):

    def setup_configuration():
        Configuration.load_instance(kwargs)
        return Configuration.get_instance()
    
    def setup_run_report():
        RunReport.load_instance()
        return RunReport.get_instance()

    def setup_output_directory(configuration):
        output_dir = configuration.get_output_dir()
        force = configuration.get_force()

        if os.path.exists(output_dir):
            if force:
                os.remove(output_dir)
                os.makedirs(output_dir)
            else:
                raise Exception("Output directory %s already exists" % output_dir)
        else:
            os.makedirs(output_dir)

    def handle():
        try:
            
            configuration = setup_configuration()
            run_report = setup_run_report()
            setup_output_directory(configuration)

            

            # run_report.set_started(TimeUtils.get_timestamp())
            # run_report.set_finished(TimeUtils.get_timestamp())
            
            # for server in configuration.get_run_config().get_servers():
            #    print(server.get_name())
            

        except Exception as e:
            print("exiting program: " + str(e))
            sys.exit(1)
    
    handle()
