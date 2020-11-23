class Summary(object):

    def __init__(self):
        self.run = 0
        self.incomplete = 0
        self.passed = 0
        self.warned = 0
        self.failed = 0
        self.skipped = 0

    def increment_incomplete(self, n=1):
        self.incomplete += n
        self.__increment_run(n)
    
    def increment_passed(self, n=1):
        self.passed += n
        self.__increment_run(n)

    def increment_warned(self, n=1):
        self.warned += n
        self.__increment_run(n)

    def increment_failed(self, n=1):
        self.failed += n
        self.__increment_run(n)

    def increment_skipped(self, n=1):
        self.skipped += n
        self.__increment_run(n)

    def __increment_run(self, n):
        self.run += n
    
    # SETTERS AND GETTERS
    
    def get_incomplete(self):
        return self.incomplete
    
    def get_passed(self):
        return self.passed
    
    def get_warned(self):
        return self.warned
    
    def get_failed(self):
        return self.failed
    
    def get_skipped(self):
        return self.skipped
