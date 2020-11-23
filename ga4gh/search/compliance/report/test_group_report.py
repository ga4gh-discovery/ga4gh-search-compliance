from ga4gh.search.compliance.report.summary import Summary

class TestGroupReport(object):

    def __init__(self):
        self.name = ""
        self.test_case_reports = []
        self.summary = None
    
    def summarize(self):
        summary = Summary()
        increment_fns = [
            summary.increment_incomplete,
            summary.increment_passed,
            summary.increment_warned,
            summary.increment_failed,
            summary.increment_skipped
        ]
        for test_case_report in self.get_test_case_reports():
            status = test_case_report.get_status()
            increment_fns[status]()
        self.summary = summary
    
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
    
    def get_summary(self):
        return self.summary
