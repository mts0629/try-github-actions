#!/usr/bin/env python


import pytest
import sys

# Add parent directory of the python sources to searching directory
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))

from uint.uint import Uint


def test_uint_init() -> None:
    """Test initializatin of Uint."""
    uint = Uint(1)

    assert uint.value() == 1


def test_uint_init_fails_with_negative_value() -> None:
    """Test initializatin of Uint fails by using negative value."""
    with pytest.raises(ValueError, match=r"Uint must be initialized with positive integer"):
        _ = Uint(-1)


def test_uint_add() -> None:
    """Test addition of an another Uint object."""
    augend = Uint(1)
    addend = Uint(1)

    assert augend.add(addend).value() == 2
    assert augend.add(Uint(2)).value() == 3


def test_uint_sub() -> None:
    """Test subtraction of an another Uint object."""
    minuend = Uint(2)
    subtrahend = Uint(1)

    assert minuend.sub(subtrahend).value() == 1


def test_uint_sub_fails_when_negative_result() -> None:
    """Test subtraction of an another Uint object fails when the value of subtrahend > minuend."""
    minuend = Uint(1)
    subtrahend = Uint(2)

    with pytest.raises(ArithmeticError, match=r"Subtrahend \(2\) is larger than minuend \(1\)"):
        _ = minuend.sub(subtrahend)
