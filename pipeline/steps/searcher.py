from dataclasses import dataclass
from pathlib import Path


@dataclass
class Searcher:
    base_path: Path
    filename: str

    def search(self) -> str:
        li = list(self.base_path.glob(self.filename))

        if len(li) != 1:
            raise FileNotFoundError(path)

        return csv_list[0]
