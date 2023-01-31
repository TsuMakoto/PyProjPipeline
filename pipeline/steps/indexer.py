from typing import Generic, Set, TypeVar

import numpy as np

from .element import Element

T = TypeVar("T", bound=Element)


class Indexer(Generic[T]):
    def __init__(self, sets: Set[T]):
        self.sets = sets
        self.table = self._make()
        self.finder = self._regist()

    def _make(self):
        return {}

    def _regist(self):
        finder = {"index": np.empty(len(self.sets), dtype=Element)}
        for elm in self.sets:
            finder["index"][elm.index] = elm
        return finder

    def find(self, index) -> T:
        return self.finder["index"][index]

    def where(self, **kwargs) -> Set[T]:
        __sets = set() | self.sets
        for k in kwargs:
            __sets &= {x for x in self.sets if getattr(x, k) == kwargs[k]}
        return __sets

    def search(self, condition) -> Set[T]:
        return {x for x in self.sets if condition(x)}

    def where_not(self, **kwargs) -> Set[T]:
        return self.sets - self.where(**kwargs)

    def compile(self, *args):
        pass

    def __getitem__(self, key) -> T:
        return self.table[key]

    def __iter__(self):
        return iter(self.table)

    def size(self):
        return len(self.table)
