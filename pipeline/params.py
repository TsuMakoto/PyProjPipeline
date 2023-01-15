from dataclasses import dataclass

from .input import Input
from .output import Output


@dataclass
class Params:
    inputs: dict[str, Input]
    outputs: dict[str, Output]
