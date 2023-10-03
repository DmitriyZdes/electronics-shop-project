"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


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
