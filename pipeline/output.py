from dataclasses import dataclass, field
from typing import Dict, List, Type

from .steps.indexer import Indexer


@dataclass
class Output:
    indexer: Type[Indexer]
    args_keys: List[str] = field(default_factory=list)
    appendix: Dict = field(default_factory=dict)
