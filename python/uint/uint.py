#!/usr/bin/env python


from __future__ import annotations


class Uint:
    """A container of unsigned integer."""
    def __init__(self, value: int):
        if value < 0:
            raise ValueError("Uint must be initialized with positive integer")
        self.__value: int = value


    def value(self) -> None:
        """Get the value."""
        return self.__value


    def add(self, addend: Uint) -> int:
        """Add a value of another Uint object."""
        return Uint(self.__value + addend.__value)


    def sub(self, subtrahend: Uint) -> int:
        """Subtract a value of another Uint object."""
        if self.__value < subtrahend.__value:
            raise ArithmeticError(f"Subtrahend ({subtrahend.__value}) is larger than minuend ({self.__value})")
        return Uint(self.__value - subtrahend.__value)
