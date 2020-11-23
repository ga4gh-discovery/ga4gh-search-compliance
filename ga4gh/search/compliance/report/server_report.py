from ga4gh.search.compliance.report.summary import Summary

class ServerReport(object):

    def __init__(self):
        self.name = ""
        self.url = ""
        self.test_group_reports = {}
        self.summary = None
    
    def summarize(self):
        summary = Summary()
        increment_fns = [
            summary.increment_incomplete,
            summary.increment_passed,
            summary.increment_warned,
            summary.increment_failed,
            summary.increment_skipped,
        ]
        for key in self.get_test_group_reports().keys():
            tg_summary = self.get_test_group_report(key).get_summary()
            getters = [
                tg_summary.get_incomplete,
                tg_summary.get_passed,
                tg_summary.get_warned,
                tg_summary.get_failed,
                tg_summary.get_skipped,
            ]
            for i in range(0, 5):
                n = getters[i]()
                increment_fns[i](n=n)

        self.summary = summary
    
    # SETTERS AND GETTERS

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_url(self, url):
        self.url = url
    
    def get_url(self):
        return self.url
    
    def add_test_group_report(self, key, test_group_report):
        self.test_group_reports[key] = test_group_report
    
    def get_test_group_reports(self):
        return self.test_group_reports
    
    def get_test_group_report(self, key):
        return self.test_group_reports[key]
