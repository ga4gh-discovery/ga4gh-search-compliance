class RunReport(object):
    """Global singleton holding all data to be output in report"""

    __instance = None

    @staticmethod
    def get_instance():
        if RunReport.__instance == None:
            raise Exception("RunReport not yet loaded, use RunReport.load_instance")
        return RunReport.__instance
    
    @staticmethod
    def load_instance():
        if RunReport.__instance != None:
            raise Exception("RunReport already loaded, use RunReport.get_instance")
        else:
            run_report = RunReport()
            RunReport.__instance = run_report

    def __init__(self):
        if RunReport.__instance != None:
            raise Exception("RunReport already loaded, use RunReport.get_instance")
        else:
            self.__set_all_props()
    
    def __set_all_props(self):
        self.started = None
        self.finished = None
        self.server_reports = []

    # SETTERS AND GETTERS

    def set_started(self, started):
        self.started = started
    
    def get_started(self):
        return self.started
    
    def set_finished(self, finished):
        self.finished = finished
    
    def get_finished(self):
        return self.finished
    
    def add_server_report(self, server_report):
        self.server_reports.append(server_report)
    
    def get_server_reports(self):
        return self.server_reports
    
    def get_server_report(self, i):
        return self.server_reports[i]
