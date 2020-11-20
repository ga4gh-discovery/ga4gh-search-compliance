class TestCaseReport(object):

    STATUS_INCOMPLETE = 0
    STATUS_PASS = 1
    STATUS_WARN = 2
    STATUS_FAIL = 3
    STATUS_SKIP = 4

    def __init__(self):
        self.name = ""
        self.description = ""
        self.status = TestCaseReport.STATUS_INCOMPLETE
        self.message = ""
        self.log_messages = []
    
    # SETTERS AND GETTERS

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_description(self, description):
        self.description = description
    
    def get_description(self):
        return self.description
    
    def set_status(self, status):
        self.status = status
    
    def get_status(self):
        return self.status
    
    def set_message(self, message):
        self.message = message
    
    def add_log_message(self, log_message):
        self.log_messages.append(log_message)
    
    def get_log_messages(self):
        return self.log_messages
