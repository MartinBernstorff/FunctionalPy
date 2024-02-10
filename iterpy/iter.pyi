"""
This type stub file was generated by pyright.
"""

from collections.abc import (
    Callable,
    Iterable,
    Iterator,
    Sequence,
)
from types import UnionType
from typing import Generic, TypeVar, overload

S = TypeVar("S")
T = TypeVar("T")
U = TypeVar("U")

iterpyables: UnionType = (
    Iterable | Iterator | "Iter" | tuple | list | set | frozenset
)

class Iter(Generic[T]):
    def __init__(self, iterable: Iterable[T]) -> None: ...
    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Iter[T]: ...
    def __iter__(self) -> Iter[T]: ...
    def __next__(self) -> T: ...
    def count(self) -> int: ...
    def to_list(self) -> list[T]: ...
    def to_tuple(self) -> tuple[T, ...]: ...
    def to_consumable(self) -> Iterator[T]: ...
    def to_set(self) -> set[T]: ...
    def map(self, func: Callable[[T], S]) -> Iter[S]: ...
    def pmap(self, func: Callable[[T], S]) -> Iter[S]: ...
    def filter(self, func: Callable[[T], bool]) -> Iter[T]: ...
    def reduce(self, func: Callable[[T, T], T]) -> T: ...
    def take(self, n: int) -> Iter[T]: ...
    def rev(self) -> Iter[T]: ...
    def any(self, func: Callable[[T], bool]) -> bool: ...
    def all(self, func: Callable[[T], bool]) -> bool: ...
    def unique(self) -> Iter[T]: ...
    def unique_by(self, func: Callable[[T], U]) -> Iter[T]: ...
    def enumerate(self) -> Iter[tuple[int, T]]: ...
    def find(self, func: Callable[[T], bool]) -> T: ...
    def last(self) -> T: ...
    def sum(self) -> T: ...
    def groupby(
        self, func: Callable[[T], str]
    ) -> Iter[tuple[str, list[T]]]: ...

    # Code for generating the following is in _generate_pyi.py
    # Iterable[S]   # noqa: ERA001
    @overload
    def flatten(self: Iter[Iterable[S]]) -> Iter[S]: ...
    @overload
    def flatten(self: Iter[Iterable[S] | S]) -> Iter[S]: ...

    # Iterator[S]   # noqa: ERA001
    @overload
    def flatten(self: Iter[Iterator[S]]) -> Iter[S]: ...
    @overload
    def flatten(self: Iter[Iterator[S] | S]) -> Iter[S]: ...

    # tuple[S, ...]   # noqa: ERA001
    @overload
    def flatten(self: Iter[tuple[S, ...]]) -> Iter[S]: ...
    @overload
    def flatten(self: Iter[tuple[S, ...] | S]) -> Iter[S]: ...

    # Sequence[S]   # noqa: ERA001
    @overload
    def flatten(self: Iter[Sequence[S]]) -> Iter[S]: ...
    @overload
    def flatten(self: Iter[Sequence[S] | S]) -> Iter[S]: ...

    # list[S]   # noqa: ERA001
    @overload
    def flatten(self: Iter[list[S]]) -> Iter[S]: ...
    @overload
    def flatten(self: Iter[list[S] | S]) -> Iter[S]: ...

    # set[S]   # noqa: ERA001
    @overload
    def flatten(self: Iter[set[S]]) -> Iter[S]: ...
    @overload
    def flatten(self: Iter[set[S] | S]) -> Iter[S]: ...

    # frozenset[S]   # noqa: ERA001
    @overload
    def flatten(self: Iter[frozenset[S]]) -> Iter[S]: ...
    @overload
    def flatten(self: Iter[frozenset[S] | S]) -> Iter[S]: ...

    # Iter[S]   # noqa: ERA001
    @overload
    def flatten(self: Iter[Iter[S]]) -> Iter[S]: ...
    @overload
    def flatten(self: Iter[Iter[S] | S]) -> Iter[S]: ...

    # str
    @overload
    def flatten(self: Iter[str]) -> Iter[str]: ...
    @overload
    def flatten(self: Iter[str | S]) -> Iter[S]: ...

    # Generic
    @overload
    def flatten(self: Iter[S]) -> Iter[S]: ...
