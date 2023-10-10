from src.item import Item
from src.phone import Phone

item_1 = Item("Смартфон", 50000.4, 30)
phone_2 = Phone("Iphone", 100000.6, 20, 10)
assert phone_2 + item_1 == 50
phone_2.sim_count = 20
assert phone_2.sim_count == 20
