from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, sim_count: int) -> None:
        """Магический метод инициализации с расширением атрибутов"""

        super().__init__(name, price, quantity)
        self.__sim_count = sim_count

    @property
    def sim_count(self):
        return self.__sim_count

    @sim_count.setter
    def sim_count(self, number_sim):
        """Сеттер для sim_count с проверкой на положительное и целое число"""

        if number_sim > 0 and isinstance(number_sim, int):
            self.__sim_count = number_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым и положительным числом")

    def __add__(self, other):
        """Магический метод сложения экземпляров базового и дочернего класса"""

        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise ValueError("Данный класс не относится к заявленным")
