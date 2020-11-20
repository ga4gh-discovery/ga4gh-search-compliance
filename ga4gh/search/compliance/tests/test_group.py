from ga4gh.search.compliance.report.test_group_report import TestGroupReport

class TestGroup(object):
    
    def __init__(self, server_config):
        self.server_config = server_config
        self.name = ""
        self.test_cases = []
    
    def execute_test_group(self):

        test_group_report = TestGroupReport()
        test_group_report.set_name(self.get_name())
        for test_case in self.test_cases:
            test_case.set_server_config(self.get_server_config())
            test_case_report = test_case.execute_test_case()
            test_group_report.add_test_case_report(test_case_report)
        return test_group_report
    
    # SETTERS AND GETTERS

    def set_server_config(self, server_config):
        self.server_config = server_config
    
    def get_server_config(self):
        return self.server_config
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def add_test_case(self, test_case):
        self.test_cases.append(test_case)
    
    def get_test_cases(self):
        return self.test_cases
