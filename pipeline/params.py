from dataclasses import dataclass
from typing import Dict

from .input import Input
from .output import Output


@dataclass
class Params:
    inputs: Dict[str, Input]
    outputs: Dict[str, Output]
