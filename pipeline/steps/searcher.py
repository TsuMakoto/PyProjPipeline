from dataclasses import dataclass
from pathlib import Path


@dataclass
class Searcher:
    base_path: Path
    filename: str

    def __post_init__(self):
        self.filepath = self.base_path / self.filename

    def search(self) -> str:
        li = list(self.base_path.glob(self.filename))

        if len(li) != 1:
            raise FileNotFoundError(self.filepath)

        return li[0]
