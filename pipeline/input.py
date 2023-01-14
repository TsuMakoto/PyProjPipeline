from dataclasses import dataclass
from io import StringIO
from pathlib import Path
from typing import Union

from pandas import DataFrame
from pandas.core.series import Series

from ..steps.element import Element
from ..steps.reader import Reader
from ..steps.searcher import Searcher


@dataclass
class Input:
    path: str
    name: str
    extension: str = "csv"

    def search(self) -> str:
        path = Path(self.path)
        searcher = self._searcher(path, f"{self.name}*.{self.extension}")
        return searcher.search()

    def read(self, file: str) -> DataFrame:
        reader = self._reader(file)
        reader.read()
        return reader.df

    def build_set(self, df: DataFrame) -> set:
        index = 0

        elements = []
        for _, row in df.iterrows():
            element = self._element(index, row)
            elements.append(element)

        return set(elements)

    def _searcher(self, base_path: Path, filename: str) -> Searcher:
        return Searcher(base_path, filename)

    def _reader(self, filepath_or_buffer: Union[str, StringIO]) -> Reader:
        return Reader(filepath_or_buffer)

    def _element(self, index: int, row: Series) -> Element:
        return Element(index, row)
