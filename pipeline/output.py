from dataclasses import dataclass, field

from .steps.appendix import Appendix


@dataclass
class Output:
    appendix: Appendix
    args_keys: list[str] = field(default_factory=list)
