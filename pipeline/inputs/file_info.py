from dataclasses import dataclass
from pathlib import Path

from ..steps.reader import Reader


@dataclass
class FileInfo:
    path: str
    name: str
    extension: str = "csv"

    def search(self) -> Reader:
        path = Path(self.path)

        csv_list = list(path.glob(f"{self.name}*.{self.extension}"))

        if len(csv_list) != 1:
            raise FileNotFoundError(path)

        return self._reader(csv_list[0])

    @property
    def _reader(self):
        return Reader
