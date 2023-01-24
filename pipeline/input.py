from dataclasses import dataclass
from pathlib import Path
from typing import Type

from pandas import DataFrame

from .steps.element import Element
from .steps.reader import Reader
from .steps.searcher import Searcher


@dataclass
class Input:
    path: str
    name: str
    extension: str = "csv"
    searcher: Type[Searcher] = Searcher
    reader: Type[Reader] = Reader
    element: Type[Element] = Element

    def search(self) -> str:
        path = Path(self.path)
        searcher = self.searcher(path, f"{self.name}*.{self.extension}")
        return searcher.search()

    def read(self, file: str) -> DataFrame:
        reader = self.reader(file)
        return reader.read(self.extension)

    def build_set(self, df: DataFrame) -> set:
        index = 0

        elements = []
        for _, row in df.iterrows():
            element = self.element(index, row)
            elements.append(element)
            index += 1

        return set(elements)
