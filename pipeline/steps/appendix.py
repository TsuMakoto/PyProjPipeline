from abc import ABCMeta, abstractmethod


class Appendix(metaclass=ABCMeta):
    def __init__(self, *args):
        self.appendix = {}

    @abstractmethod
    def post_init(self, *args):
        pass
