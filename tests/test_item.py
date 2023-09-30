"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

def test_calculate_total_price():
    item_1 = Item("Cмартфон", 45000.8, 10)
    assert item_1.calculate_total_price() == 450008.0

def test_apply_discount():
    item_2 = Item("Телефизор", 20000.5, 50)
    assert item_2.apply_discount() == 20000.5