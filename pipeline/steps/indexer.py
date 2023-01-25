from typing import Generic, Set, TypeVar

from .element import Element

T = TypeVar("T", bound=Element)


class Indexer(Generic[T]):
    def __init__(self, sets: Set[T]):
        self.sets = sets
        self.table = self._make()

    def _make(self):
        return {}

    def compile(self, *args):
        pass

    def __getitem__(self, key) -> T:
        return self.table[key]

    def __iter__(self):
        return iter(self.table)

    def size(self):
        return len(self.table)
