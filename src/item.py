import csv
import os


class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = 'Файл item.csv поврежден'
        print(self.message)


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    file = 'items.csv'

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
        super().__init__()

    def __repr__(self):
        return f'{self.__class__.__name__}{self.__name, self.price, self.quantity}'

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от него.')
        return self.quantity + other.quantity

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
    def instantiate_from_csv(cls, file_name=file):
        path_to_dir = os.path.join(os.path.dirname(__file__), file_name)
        if not os.path.exists(path_to_dir):
            raise FileNotFoundError('Отсутствует файл item.csv')
        with open(path_to_dir, newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if not 'name' in row or not 'price' in row or not 'quantity' in row:
                    raise InstantiateCSVError
                new_instance = cls(row['name'], float(row['price']), int(row['quantity']))
                cls.all.append(new_instance)

    @staticmethod
    def string_to_number(number_str: str):
        return int(float(number_str))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, product_name: str) -> None:
        if len(product_name) > 10:
            self.__name = product_name[:10]
        else:
            self.__name = product_name
