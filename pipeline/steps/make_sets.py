from dataclasses import dataclass
from typing import List

from steps.reader import Reader


@dataclass
class MakeSets:
    readers: List[Reader]


