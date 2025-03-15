import doctest


class Book:
    def __init__(self, title: str, author: str, year: int):
        """
        Конструктор класса Book.

        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год выпуска книги. Должно быть неотрицательным числом.

        :raises ValueError: Если год не целое или отрицательное число.
        """
        if year <= 0:
            raise ValueError("Год печати должен быть неотрицательным числом.")
        self.title = title
        self.author = author
        self.year = year

    def get_discription(self) -> str:
        """
        Возвращает краткое описание книги.

        :return: Строка с описанием книги.

        Пример:
        >>> book = Book("Анна Каренина", "Лев Толстой", 1878)
        >>> book.get_discription()
        'Книга "Анна Каренина" написана автором Лев Толстой, напечатана в 1878.'
        """
        return f'Книга "{self.title}" написана автором {self.author}, напечатана в {self.year}.'

    def is_old(self, year: int = 2018) -> bool:
        """
        Проверяет, является ли книга старой.

        :param year: Год до которого книги старые. По умолчанию 2018.
        :return: True, если год печати меньше порога, иначе False.

        Пример:
        >>> book = Book("Анна Каренина", "Лев Толстой", 1878)
        >>> book.is_old()
        True
        """
        return self.year < year


class Car:
    def __init__(self, brand: str, model: str, fuel_level: float):
        """
        Конструктор класса Car.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param fuel_level: Уровень топлива в баке. Должен быть в диапазоне от 0 до 100%.

        :raises ValueError: Если уровень топлива выходит за допустимые пределы.
        """
        if not 0 <= fuel_level <= 100:
            raise ValueError("Уровень топлива должен быть в диапазоне от 0 до 100%")
        self.brand = brand
        self.model = model
        self.fuel_level = fuel_level

    def refuel(self, fuel: float) -> None:
        """
        Заправляет автомобиль на указанное количество процентов.

        :param fuel: Количество процентов для заправки. Должно быть положительным числом.

        :raises ValueError: Если количество топлива для заправки неположительное.

        Пример:
        >>> car = Car("ГАЗ", "Волга", 50.0)
        >>> car.refuel(30)
        >>> car.fuel_level
        80.0
        """
        if fuel <= 0:
            raise ValueError("Количество топлива для заправки должно быть положительным.")
        self.fuel_level = min(self.fuel_level + fuel, 100)

    def can_drive(self, distance: float, fuel_consumption: float = 10) -> bool:
        """
        Проверяет, может ли автомобиль проехать указанное расстояние.

        :param distance: Расстояние в километрах.
        :param fuel_consumption: Расход топлива на 100 км. По умолчанию 10 л/100 км.
        :return: True, если топлива достаточно, иначе False.

        Пример:
        >>> car = Car("ГАЗ", "Волга", 50.0)
        >>> car.can_drive(500)
        True
        """
        required_fuel = (distance * fuel_consumption) / 100
        return self.fuel_level >= required_fuel


class Bank_Account:
    def __init__(self, owner: str, balance: float = 0.0):
        """
        Конструктор класса BankAccount.

        :param owner: Владелец счета.
        :param balance: Начальный баланс счета. По умолчанию 0.0.

        :raises ValueError: Если начальный баланс отрицательный.
        """
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Пополняет счет на указанную сумму.

        :param amount: Сумма для пополнения. Должна быть положительной.

        :raises ValueError: Если сумма для пополнения отрицательная.

        Пример:
        >>> account = Bank_Account("Darth Vader", 10.0)
        >>> account.deposit(5)
        >>> account.balance
        15.0
        """
        if amount < 0:
            raise ValueError("Сумма для пополнения должна быть положительной.")
        self.balance += amount

    def withdraw(self, amount: float) -> float:
        """
        Снимает указанную сумму со счета.

        :param amount: Сумма для снятия. Должна быть положительной и не превышать баланс.

        :raises ValueError: Если сумма для снятия отрицательная или превышает баланс.
        :return: Снятая сумма.

        Пример:
        >>> account = Bank_Account("Darth Vader", 10.0)
        >>> account.withdraw(10)
        10
        >>> account.balance
        0.0
        """
        if amount < 0:
            raise ValueError("Сумма для снятия должна быть положительной.")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете.")
        self.balance -= amount
        return amount


if __name__ == "__main__":
    doctest.testmod()
