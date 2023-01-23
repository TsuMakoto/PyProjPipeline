from dataclasses import dataclass, field
from typing import List

from .steps.appendix import Appendix


@dataclass
class Output:
    appendix: Appendix
    args_keys: List[str] = field(default_factory=list)
