import functools

class FunctionBinder(object):

    @staticmethod
    def bind(func, *args):
        return functools.partial(func, *args)