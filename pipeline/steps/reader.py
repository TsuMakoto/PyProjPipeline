from dataclasses import dataclass
from io import StringIO
from typing import Union

import pandas as pd
from pd.core.series import Series
from utils.io import load_df


@dataclass
class Element:
    index: int
    row: Series


class ElementBuilder:
    @property
    def element(self) -> Element:
        return self.element

    @element.setter
    def element(self, element: Element):
        self.element = element

    @property
    def index(self) -> int:
        return self.index

    @index.setter
    def index(self, index: int):
        self.index = index

    @property
    def row(self) -> Series:
        return self.row

    @row.setter
    def row(self, row: Series):
        self.row = row

    def build(self):
        self.element.index = self.index
        self.element.row = self.row

        return self.element


@dataclass
class Reader:
    filepath_or_buffer: Union[str, StringIO]

    def __post_init__(self):
        df = load_df(self.filepath_or_buffer)
        df = df.fillna(0)

        self.df = df

        index = 0
        buidler = ElementBuilder()
        elements = []
        for _, row in df.iterrows():
            buidler.element = self._element()
            builder.index = index
            builder.row = row
            element = buidler.build()
            elements.append(element)
            index += 1

        self.sets = set(elements)

    def _element(self) -> Element:
        return Element()
