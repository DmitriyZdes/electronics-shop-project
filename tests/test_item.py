"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item, InstantiateCSVError
import pytest

def test_calculate_total_price():
    item_1 = Item("Cмартфон", 45000.8, 10)
    assert item_1.calculate_total_price() == 450008.0


def test_apply_discount():
    item_2 = Item("Телевизор", 20000.5, 50)
    assert item_2.apply_discount() == 20000.5


def test_string_to_number():
    string = "11"
    number = 11
    assert Item.string_to_number(string) == number


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')  # создание объектов из данных файла
    assert len(Item.all) == 5

# Тесты на repr и str

item_2 = Item("Планшет", 30000.5, 10)

assert repr(item_2) == "Item('Планшет', 30000.5, 10)"
assert str(item_2) == "Планшет"

#Тесты на класс ошибок  InstantiateCSVError

def test_instatiate_csv_error():

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_csv_error('src/item1.csv')
