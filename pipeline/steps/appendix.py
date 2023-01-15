from abc import ABCMeta, abstractmethod

from pipeline.steps.element import Element


class Appendix(metaclass=ABCMeta):
    def __init__(self):
        self.appendix = {}

    @abstractmethod
    def post_init(self, sets: set[Element], *args):
        pass
