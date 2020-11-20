class StaticUtils(object):

    @staticmethod
    def add_trailing_slash(s):
        if s.endswith("/"):
            return s
        return s + "/"
    
    @staticmethod
    def remove_trailing_slash(s):
        if s.endswith("/"):
            return s[:-1]
        return s
