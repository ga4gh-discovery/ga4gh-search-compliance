from ga4gh.search.compliance.report.test_case_report import TestCaseReport

class TestCase(object):

    def __init__(self, name, description, test_method):
        self.name = name
        self.description = description
        self.test_method = test_method
        self.server_config = None
    
    def execute_test_case(self):
        test_case_report = TestCaseReport()
        test_case_report.set_name(self.get_name())
        test_case_report.set_description(self.get_description())
        self.test_method(self.get_server_config(), test_case_report)
        return test_case_report
    
    # SETTERS AND GETTERS

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_description(self, description):
        self.description = description
    
    def get_description(self):
        return self.description
    
    def set_server_config(self, server_config):
        self.server_config = server_config
    
    def get_server_config(self):
        return self.server_config
