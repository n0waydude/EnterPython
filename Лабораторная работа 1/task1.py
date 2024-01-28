import doctest
from typing import Union


# TODO Написать 3 класса с документацией и аннотацией типов
class Credit:
    def __init__(self, debt_sum: Union[int, float], monthly_percentage: Union[int, float], months_number: int):
        """
            Создание и подготовка к работе объекта "Кредит"

            :param debt_sum: Сумма долга по кредиту
            :param monthly_percentage: Проуентная ежемесячная ставка (в процентах)
            :param months_number: Количество месяцев для погашения кредита

            Примеры:
            >>> credit = Credit(10000, 20.7, 15)  # инициализация экземпляра класса
        """
        if not isinstance(debt_sum, (int, float)):
            raise TypeError("Сумма долга должна быть типа int или float")
        if debt_sum < 0:
            raise ValueError("Сумма долга не может быть отрицательным числом")
        self.debt_sum = debt_sum

        if not isinstance(monthly_percentage, (int, float)):
            raise TypeError("Процентная ставка должна быть типа int или float")
        if monthly_percentage < 0:
            raise ValueError("Процентная ставка не может быть отрицательным числом")
        self.monthly_percentage = monthly_percentage

        if not isinstance(months_number, int):
            raise TypeError("Количество месяцев должно быть типа int")
        if months_number < 0:
            raise ValueError("Количество месяцев не может быть отрицательным числом")
        self.months_number = months_number

    def is_repaid(self) -> bool:
        """
        Функция, которая проверяет, погашен ли кредит

        :return: Равна ли сумма долга нулю

        Примеры:
        >>> credit = Credit(0, 0, 0)
        >>> credit.is_repaid()
        """
        ...

    def is_early_repayment(self, sum_of_money: Union[int, float]) -> bool:
        """
        Функция, которая проверяет, можно ли погасить кредит досрочно

        :param sum_of_money: Вносимая сумма денег
        :raise ValueError: Если вносимая сумма не является положительным числом, то вызываем ошибку
        :raise TypeError: Если тип переменной не согласуется с указанным, то вызываем ошибку
        :return: Возможно ли досрочное погашение

        Примеры:
        >>> credit = Credit(10000, 20.7, 15)
        >>> credit.is_early_repayment(100000)
        """
        if not isinstance(sum_of_money, (int, float)):
            raise TypeError("Сумма денег должна быть типа int или float")
        if sum_of_money <= 0:
            raise ValueError("Сумма денег должна быть положительным числом")
        ...

    def add_money(self, sum_of_money: Union[int, float]) -> Union[int, float]:
        """
        Функция, уменьшающая сумму долга на вносимую сумму с учетом процентов

        :param sum_of_money: Вносимая сумма денег
        :raise ValueError: Если вносимая сумма не является положительным числом, то вызываем ошибку
        :raise TypeError: Если тип переменной не согласуется с указанным, то вызываем ошибку
        :return: Остаток от вносимой суммы, если она превышает сумму долга с процентами, и 0, если не превышает

        Примеры:
        >>> credit = Credit(10000, 20.7, 15)
        >>> credit.is_early_repayment(100)
        """
        ...


class Screw:
    def __init__(self, fabric: str, color: str, length: Union[int, float]):
        """
            Создание и подготовка к работе объекта "Шуруп"

            :param fabric: Материал изделия
            :param color: Цвет изделия
            :param length: Толщина изделия в сантиметрах

            Примеры:
            >>> screw = Screw('iron', 'black', 33.5)  # инициализация экземпляра класса
        """
        if not isinstance(fabric, str):
            raise TypeError("Название материала должно быть типа str")
        if fabric == '':
            raise ValueError("Название материала должно быть непустой строкой")
        self.fabric = fabric

        if not isinstance(color, str):
            raise TypeError("Название цвета должно быть типа str")
        if color == '':
            raise ValueError("Название цвета должно быть непустой строкой")
        self.color = color

        if not isinstance(length, (int, float)):
            raise TypeError("Длина изделия должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина изделия должна быть положительным числом")
        self.length = length

    def is_required_material(self, material: str) -> bool:
        """
        Функция, которая проверяет, сделан ли шуруп из нужного материала

        :param material: Требуемый материал
        :raise ValueError: Если введенная пользователем строка пустая, то вызываем ошибку
        :raise TypeError: Если тип переменной не согласуется с указанным, то вызываем ошибку
        :return: Правильный ли материал

        Примеры:
        >>> screw = Screw('iron', 'black', 33.5)
        >>> screw.is_required_material('plastic')
        """
        if not isinstance(material, str):
            raise TypeError("Название материала должно быть типа str")
        if material == '':
            raise ValueError("Название материала должно быть непустой строкой")
        ...

    def recolor_screw(self, new_color: str) -> None:
        """
        Функция, которая меняет цвет шурупа на нужный, если при проверке он не совпал с изначальным

        :param new_color: Правильный цвет
        :raise ValueError: Если введенная пользователем строка пустая, то вызываем ошибку
        :raise TypeError: Если тип переменой не согласуется с указанным, то вызываем ошибку

        Примеры:
        >>> screw = Screw('iron', 'black', 33.5)
        >>> screw.recolor_screw('yellow')
        """
        ...

    def length_delta(self, new_length: Union[int, float]) -> Union[int, float]:
        """
        Функция, сравнивает текущую длину шурупа с правильной и выдает модуль разности измерений

        :param new_length: Правильная длина
        :raise ValueError: Если нужная длина не является положительным числом, то вызываем ошибку
        :raise TypeError: Если тип переменной не согласуется с указанным, то вызываем ошибку
        :return: Абсолютная разница измерений

        Примеры:
        >>> screw = Screw('iron', 'black', 33.5)
        >>> screw.length_delta(20)
        """
        if not isinstance(new_length, (int, float)):
            raise TypeError("Длина должна быть типа int или float")
        if new_length <= 0:
            raise ValueError("Длина изделия должна быть положительным числом")
        ...


class Soup:
    def __init__(self, soup_volume: Union[int, float], temperature: Union[int, float], expiry_date: int):
        """
            Создание и подготовка к работе объекта "Суп"

            :param soup_volume: Объем супа (в мл)
            :param temperature: Температура супа (в градусах Цельсия)
            :param expiry_date: Срок хранения супа (в днях)

            Примеры:
            >>> soup = Soup(1000, -2.5, 7)  # инициализация экземпляра класса
        """
        if not isinstance(soup_volume, (int, float)):
            raise TypeError("Объем супа должен быть типа int или float")
        if soup_volume < 0:
            raise ValueError("Объем супа не может быть отрицательным числом")
        self.soup_volume = soup_volume

        if not isinstance(temperature, (int, float)):
            raise TypeError("Значение температуры должно быть типа int или float")
        self.temperature = temperature

        if not isinstance(expiry_date, int):
            raise TypeError("Срок хранения должен быть типа int")
        if expiry_date < 0:
            raise ValueError("Срок хранения не может быть отрицательным числом")
        self.expiry_date = expiry_date

    def is_dishes_empty(self) -> bool:
        """
        Функция, которая проверяет, закончился ли суп

        :return: Равен ли объем супа нулю

        Примеры:
        >>> soup = Soup(0, 0, 0)
        >>> soup.is_dishes_empty()
        """
        ...

    def checking_date(self, days: int) -> Union[int, str]:
        """
        Функция, которая проверяет, сколько еще дней может храниться суп

        :param days: Сколько дней уже хранится суп
        :raise ValueError: Если количество дней не является положительным числом, то вызываем ошибку
        :raise TypeError: Если тип переменной не согласуется с указанным, то вызываем ошибку
        :return: Разность между сроком годности и введенным значением, если срок больше введенного значения,
        и сообщение 'просрочен', если меньше

        Примеры:
        >>> soup = Soup(1000, -2.5, 7)
        >>> soup.checking_date(5)
        """
        if not isinstance(days, int):
            raise TypeError("Количество дней должно быть типа int")
        if days <= 0:
            raise ValueError("Количество дней должно быть положительным числом")
        ...

    def heating(self, rise_temperature: Union[int, float]) -> None:
        """
        Функция, увеличивающая значение температуры до указанного

        :param rise_temperature: Нужная температура
        :raise ValueError: Если нужная температура не больше изначальной, то вызываем ошибку
        :raise TypeError: Если тип переменной не согласуется с указанным, то вызываем ошибку

        Примеры:
        >>> soup = Soup(1000, -2.5, 7)
        >>> soup.heating(20)
        """
        if not isinstance(rise_temperature, (int, float)):
            raise TypeError("Значение температуры должно быть типа int или float")
        if rise_temperature <= self.temperature:
            raise ValueError("Нужная температура должна быть больше изначальной")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
   