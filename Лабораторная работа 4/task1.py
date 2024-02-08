import doctest
from typing import Union


class Watch:
    def __init__(self, hours: int, minutes: int, seconds: int):
        """
            Создание и подготовка к работе объекта "Часы"

            :param hours: Время в часах
            :param minutes: Время в минутах
            :param seconds: Время в секундах

            Примеры:
            >>> watch = Watch(5, 13, 48)  # инициализация экземпляра класса
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self) -> str:
        """
            Метод, представляющий данные атрибутов класса в виде понятной пользователю строки

            :return: Строка, показывающая текущее время на часах
        """
        return f"Время: {self.hours} часов, {self.minutes} минут, {self.seconds} секунд"

    def __repr__(self) -> str:
        """
            Метод, отображающий название текущего класса, а также его пользовательских атрибутов

            :return: Строка, показывающая текущий класс и его атрибуты
        """
        return f"{self.__class__.__name__}({self.__dict__})"

    """
        Свойства для установки и чтения данных для атрибутов класса, а также проверка значений 
    """
    @property
    def hours(self) -> int:
        return self._hours

    @hours.setter
    def hours(self, current_hours: int) -> None:
        if not isinstance(current_hours, int):
            raise TypeError("Количество часов должно быть типа int")
        if not 0 <= current_hours <= 23:
            raise ValueError("Количество часов должно находиться в диапазоне от 0 до 23")
        self._hours = current_hours

    @property
    def minutes(self) -> int:
        return self._minutes

    @minutes.setter
    def minutes(self, current_minutes: int) -> None:
        if not isinstance(current_minutes, int):
            raise TypeError("Количество минут должно быть типа int")
        if not 0 <= current_minutes <= 59:
            raise ValueError("Количество минут должно находиться в диапазоне от 0 до 59")
        self._minutes = current_minutes

    @property
    def seconds(self) -> int:
        return self._seconds

    @seconds.setter
    def seconds(self, current_seconds: int) -> None:
        if not isinstance(current_seconds, int):
            raise TypeError("Количество секунд должно быть типа int")
        if not 0 <= current_seconds <= 59:
            raise ValueError("Количество секунд должно находиться в диапазоне от 0 до 59")
        self._seconds = current_seconds

    def is_accurate_time(self, hours: int, minutes: int, seconds: int) -> bool:
        """
        Функция, которая проверяет, точное ли время показывают часы

        :raise ValueError: Если указанные числа не входят в нужные интервалы (для часов - от 0 до 23,
         для минут и секунд - от 0 до 59), то вызываем ошибку
        :raise TypeError: Если тип переменных не согласуется с указанным, то вызываем ошибку
        :return: Точное ли время на циферблате

        Примеры:
        >>> watch = Watch(5, 13, 48)
        >>> watch.is_accurate_time(17, 50, 3)
        """
        ...


class WristWatch(Watch):
    def __init__(self, hours: int, minutes: int, seconds: int, strap_length: Union[int, float]):
        """
            Создание и подготовка к работе объекта "Наручные часы"

            :param hours: Время в часах
            :param minutes: Время в минутах
            :param seconds: Время в секундах
            :param strap_length: Длина ремешка (в см)

            Примеры:
            >>> wrist_watch = WristWatch(5, 13, 48, 10.1)  # инициализация экземпляра класса
        """
        super().__init__(hours, minutes, seconds)
        self.strap_length = strap_length

    def __str__(self) -> str:
        """
            Перегруженный метод класса Watch, показывающий как время, так и длину ремешка часов

            :return: Строка, показывающая текущее время на часах и длину ремешка
        """
        return f"Время: {self.hours} часов, {self.minutes} минут, {self.seconds} секунд. " \
               f"Длина ремешка: {self.strap_length} сантиметров"

    """
        Свойства для установки и чтения данных для атрибута strap_length, а также проверка значения 
    """
    @property
    def strap_length(self) -> Union[int, float]:
        return self._strap_length

    @strap_length.setter
    def strap_length(self, current_length: Union[int, float]) -> None:
        if not isinstance(current_length, (int, float)):
            raise TypeError("Длина должна быть типа int или float")
        if current_length <= 0:
            raise ValueError("Длина должна быть положительным числом")
        self._strap_length = current_length

    def length_delta(self, new_length: Union[int, float]) -> Union[int, float]:
        """
        Функция, сравнивает текущую длину ремешка с правильной и выдает модуль разности измерений

        :param new_length: Правильная длина
        :raise ValueError: Если нужная длина не является положительным числом, то вызываем ошибку
        :raise TypeError: Если тип переменной не согласуется с указанным, то вызываем ошибку
        :return: Абсолютная разница измерений

        Примеры:
        >>> wrist_watch = WristWatch(5, 13, 48, 10.1)
        >>> wrist_watch.length_delta(9.5)
        """
        if not isinstance(new_length, (int, float)):
            raise TypeError("Длина ремешка должна быть типа int или float")
        if new_length <= 0:
            raise ValueError("Длина ремешка должна быть положительным числом")
        ...


class ElWatch(WristWatch):
    def __init__(self, hours: int, minutes: int, seconds: int, strap_length: Union[int, float], screen_on: bool):
        """
            Создание и подготовка к работе объекта "Электронные часы"

            :param hours: Время в часах
            :param minutes: Время в минутах
            :param seconds: Время в секундах
            :param strap_length: Длина ремешка (в см)
            :param screen_on: Светится ли экран часов (вкл/выкл)

            Примеры:
            >>> el_watch = ElWatch(5, 13, 48, 10.1, True)  # инициализация экземпляра класса
        """
        super().__init__(hours, minutes, seconds, strap_length)
        self.screen_on = screen_on

    def __str__(self) -> str:
        """
            Перегруженный метод класса WristWatch, показывающий как время и длину ремешка часов, так и
            состояние экрана (вкл/выкл)

            :return: Строка, показывающая текущее время на часах, длину ремешка и состояние экрана
        """
        return f"Время: {self.hours} часов, {self.minutes} минут, {self.seconds} секунд. " \
               f"Длина ремешка: {self.strap_length} сантиметров. Экран светится: {self.screen_on}"

    """
        Свойства для установки и чтения данных для атрибута screen_on, а также проверка значения 
    """
    @property
    def screen_on(self) -> bool:
        return self._screen_on

    @screen_on.setter
    def screen_on(self, on_off: bool) -> None:
        if not isinstance(on_off, bool):
            raise TypeError("Индикатор горящего экрана должен быть типа bool")
        self._screen_on = on_off

    def is_accurate_time(self, hours: int, minutes: int, seconds: int) -> Union[bool, int]:
        """
            Перегруженная функция класса Watch, которая проверяет, точное ли время показывают часы при наличии
            горящего экрана

            :raise ValueError: Если указанные числа не входят в нужные интервалы (для часов - от 0 до 23,
            для минут и секунд - от 0 до 59), то вызываем ошибку
            :raise TypeError: Если тип переменных не согласуется с указанным, то вызываем ошибку
            :return: Точное ли время на циферблате при условии, что параметр screen_on в состоянии True;
            0, есдли экран выключен (screen_on в состоянии False)

            Примеры:
            >>> el_watch = ElWatch(5, 13, 48, 10.1, True)
            >>> el_watch.is_accurate_time(17, 50, 3)
        """
        ...


class WallClock(Watch):
    def __init__(self, hours: int, minutes: int, seconds: int, shape: str):
        """
            Создание и подготовка к работе объекта "Настенные часы"

            :param hours: Время в часах
            :param minutes: Время в минутах
            :param seconds: Время в секундах
            :param shape: Форма циферблата (круг, прямоугольник и т.д.)

            Примеры:
            >>> wall_clock = WallClock(5, 13, 48, 'circle')  # инициализация экземпляра класса
        """
        super().__init__(hours, minutes, seconds)
        self.shape = shape

    def __str__(self) -> str:
        """
            Перегруженный метод класса Watch, показывающий как время, так и форму циферблата

            :return: Строка, показывающая текущее время на часах и форму циферблата
        """
        return f"Время: {self.hours} часов, {self.minutes} минут, {self.seconds} секунд. " \
               f"Форма циферблата: {self.shape}"

    """
        Свойства для установки и чтения данных для атрибута shape, а также проверка значения 
    """

    @property
    def shape(self) -> str:
        return self._shape

    @shape.setter
    def shape(self, current_shape: str) -> None:
        if not isinstance(current_shape, str):
            raise TypeError("Форма циферблата должна быть типа str")
        if current_shape == '':
            raise ValueError("Форма циферблата должна быть непустой строкой")
        self._shape = current_shape


if __name__ == "__main__":
    # Write your solution here
    doctest.testmod()
