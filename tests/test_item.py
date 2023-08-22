"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

Item.pay_rate = 0.8


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_item1_pay_rate(item1):
    item1.apply_discount()
    assert item1.price == 8000.0


def test_item1_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000
