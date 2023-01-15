from dataclasses import dataclass, field

from pandas.core.series import Series


@dataclass(frozen=True)
class Element:
    index: int
    row: Series = field(compare=False)
