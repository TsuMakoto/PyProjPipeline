from dataclasses import dataclass, field

from pandas.core.series import Series


@dataclass(frozen=True)
class Element:
    index: int
    row: Series = field(compare=False)

    @classmethod
    def init_with_none(cls, **kwargs):
        keys = cls.__dataclass_fields__.keys()
        d = {k: kwargs.get(k) for k in keys}
        return cls(**d)
