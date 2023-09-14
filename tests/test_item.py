"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone

Item.pay_rate = 0.8


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_item1_pay_rate(item1):
    item1.apply_discount()
    assert item1.price == 8000.0


def test_item1_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    with pytest.raises(FileNotFoundError):
        assert Item.instantiate_from_csv('items_.csv')
    # with pytest.raises(InstantiateCSVError):
    #     assert Item.instantiate_from_csv('items without s.csv')
    #

item2 = Item("TV", 100000, 10)
item3 = Item("Keyboard", 5000, 5)


def test_name():
    assert item3.name == "Keyboard"


def test__repr__():
    assert repr(item2) == "Item('TV', 100000, 10)"
    assert repr(item3) == "Item('Keyboard', 5000, 5)"


def test__str__():
    assert str(item2) == 'TV'
    assert str(item3) == 'Keyboard'


phone1 = Phone("iPhone 14", 120_000, 5, 2)
item5 = Item("Смартфон", 10000, 20)


def test__add__():
    assert item5 + phone1 == 25
    assert phone1 + phone1 == 10
    with pytest.raises(ValueError):
        assert item5 + 50
