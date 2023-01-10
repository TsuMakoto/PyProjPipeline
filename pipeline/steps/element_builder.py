from dataclasses import dataclass

from pandas.core.series import Series


@dataclass
class Element:
    index: int
    row: Series


class ElementBuilder:
    def __init__(self, element: Element):
        self.element = element

    @property
    def index(self):
        return self.element.index

    @index.setter
    def index(self, index: int):
        self.element.index = index

    @property.setter
    def row(self):
        return self.element.row

    @row.setter
    def row(self, row: Series):
        self.element.row = row
