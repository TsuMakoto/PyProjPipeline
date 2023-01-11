from dataclasses import dataclass

from pd.core.series import Series


@dataclass
class Element:
    index: int
    row: Series
