class PipeOperator:
    def __init__(self, *args):
        self.args = args

    def __mul__(self, func):
        return self.__class__(*self.__execute(func))

    def __rshift__(self, func):
        return (self * func).eval()

    def eval(self):
        if len(self.args) == 1:
            return self.args[0]
        return self.args

    def __execute(self, func):
        e = func(*self.args)

        return e if isinstance(e, tuple) else [e]
