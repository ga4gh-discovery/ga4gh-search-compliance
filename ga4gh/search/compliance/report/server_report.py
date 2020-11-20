class ServerReport(object):

    def __init__(self):
        self.name = ""
        self.url = ""
        self.test_group_reports = []
    
    # SETTERS AND GETTERS

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_url(self, url):
        self.url = url
    
    def get_url(self):
        return self.url
    
    def add_test_group_report(self, test_group_report):
        self.test_group_reports.append(test_group_report)
    
    def get_test_group_reports(self):
        return self.test_group_reports
    
    def get_test_group_report(self, i):
        return self.test_group_reports[i]
