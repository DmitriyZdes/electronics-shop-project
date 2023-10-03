import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, name):
        self.__name = name
        if len(self.__name) <= 10:
            return self.__name
        else:
            return self.__name[:11]


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity


    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        return self.price * Item.pay_rate


    @classmethod
    def instantiate_from_csv(cls, filename):
        """Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv"""

        with open(filename, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            items = []
            for row in reader:
                name = str(row["name"])
                price = int(row["price"])
                quantity = int(row["quantity"])
                item = cls(name, price, quantity)
                items.append(item)
            cls.all = items


    @staticmethod
    def string_to_number(string: str) -> None:
        """Статический метод, возвращающий число из числа-строки"""

        return int(float(string))
