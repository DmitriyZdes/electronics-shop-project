import csv

class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден'

    def __str__(self):
        return self.message

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

    def __repr__(self):
        """Информация о классе для разработчиков"""

        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Информация для пользователей"""

        return self.name

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

    def __add__(self, other):
        """Магический метод сложения экземпляров базового и дочернего класса"""

        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise ValueError("Данный класс не относится к заявленным")

    @classmethod
    def instantiate_csv_error(cls, link='src/items.csv'):
        try:
            with open(link, encoding='utf-8') as file:
                line = csv.DictReader(file)
                items = []
                for row in line:
                    print(row)
                    print("name" not in row or "price" not in row or "quantity" not in row)
                    if "name" not in row or "price" not in row or "quantity" not in row:
                        print(1)
                        raise InstantiateCSVError('Повреждение данных или части данных')
                    else:
                        name = str(row["name"])
                        price = int(row["price"])
                        quantity = int(row["quantity"])
                        item = cls(name, price, quantity)
                        items.append(item)
                        cls.all = items
        except FileNotFoundError:
            print('Отсутствует файл item.csv')
        else:
            print('Код работает в штатном режиме')
        finally:
            print('Программа завершена')
