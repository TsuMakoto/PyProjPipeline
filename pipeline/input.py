from dataclasses import dataclass
from io import StringIO
from pathlib import Path
from typing import Union

from pandas.core.series import Series

from ..steps.element import Element
from ..steps.reader import Reader
from ..steps.searcher import Searcher


@dataclass
class Input:
    path: str
    name: str
    extension: str = "csv"

    def search(self):
        path = Path(self.path)
        searcher = self._searcher(path, f"{self.name}*.{self.extension}")
        self.file = searcher.search()

    def read(self):
        reader = self._reader(self.file)
        reader.read()
        self.df = reader.df

    def build_set(self):
        index = 0

        elements = []
        for _, row in self.df.iterrows():
            element = self._element(index, row)
            elements.append(element)

        self.sets = set(elements)

    def _searcher(self, base_path: Path, filename: str) -> Searcher:
        return Searcher(base_path, filename)

    def _reader(self, filepath_or_buffer: Union[str, StringIO]) -> Reader:
        return Reader(filepath_or_buffer)

    def _element(self, index: int, row: Series) -> Element:
        return Element(index, row)
