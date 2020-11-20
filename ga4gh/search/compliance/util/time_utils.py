import datetime

class TimeUtils(object):

    @staticmethod
    def get_timestamp():
        d = datetime.datetime.utcnow()
        return d.isoformat("T") + "Z"