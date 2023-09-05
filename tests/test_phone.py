import pytest

from src.phone import Phone

phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test__repr__():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
