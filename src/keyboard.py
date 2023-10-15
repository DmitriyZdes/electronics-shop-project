from src.item import Item


class KeyMixin:
    """"Класс для наследования функционала в Keyboard """
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        """Геттер для приватного атрибута language"""
        return self.__language

    def change_lang(self):
        """Метод изменения языка объекта класса Keyboard"""

        if self.__language.upper() == "EN":
            self.__language = "RU"
            return self.__language
        else:
            self.__language = "EN"


class Keyboard(Item, KeyMixin):
    """Класс для клавиатуры в магазине товаров, наследующийся от Item и доп класса Keymixin"""

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        KeyMixin.__init__(self)

    def __repr__(self):
        """Магический метод с информацией об объекте класса"""

        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, '{self.language}')"
