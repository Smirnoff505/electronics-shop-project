import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.pay_rate * self.price

    @classmethod
    def instantiate_from_csv(cls):
        result = []
        with open('../src/items.csv',
                  newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                values = row['name'], float(row['price']), int(row['quantity'])
                result.append(values)
            cls.all = result

    @staticmethod
    def string_to_number(number_str: str):
        num = []
        for letter in number_str:
            if letter.isdigit():
                num.append(letter)
            else:
                break
        number_int = int(''.join(num))
        return number_int

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, product_name: str) -> None:
        if len(product_name) > 10:
            self.__name = product_name[:10]
        else:
            self.__name = product_name
