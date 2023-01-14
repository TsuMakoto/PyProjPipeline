from dataclasses import dataclass, field

from pd.core.series import Series


@dataclass(frozen=True)
class Element:
    index: int
    row: Series = field(compare=False)
