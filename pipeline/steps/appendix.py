from dataclasses import dataclass
from typing import Dict, Set

from .reader import Element


@dataclass
class Appendix:
    sets: Set[Element]

    def __post_init__(self):
        self.__appendix: Dict[int, Element] = {}

        for elm in self.sets:
            self.__appendix[elm.index] = elm

    def __getitem__(self, element: Element):
        return self.__appendix[element.index]
