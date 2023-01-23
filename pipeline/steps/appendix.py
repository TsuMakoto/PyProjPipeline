from abc import ABCMeta, abstractmethod
from typing import Set

from .element import Element


class Appendix(metaclass=ABCMeta):
    def __init__(self):
        self.appendix = {}

    @abstractmethod
    def post_init(self, sets: Set[Element], *args):
        pass
