class TestGroupReport(object):

    def __init__(self):
        self.name = ""
        self.test_case_reports = []
    
    # SETTERS AND GETTERS

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def add_test_case_report(self, test_case_report):
        self.test_case_reports.append(test_case_report)
    
    def get_test_case_reports(self):
        return self.test_case_reports
    
    def get_test_case_report(self, i):
        return self.test_case_reports[i]
