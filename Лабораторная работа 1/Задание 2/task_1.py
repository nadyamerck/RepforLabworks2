import doctest


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Конструктор класса Book.

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц. Должно быть положительным числом.

        :raises ValueError: Если количество страниц меньше или равно 0.
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self.title = title
        self.author = author
        self.pages = pages

    def get_discription(self) -> str:
        """
        Возвращает краткое описание книги.

        :return: Строка с описанием книги.

        Пример:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.get_discription()
        'Книга "1984" написана George Orwell, содержит 328 страниц.'
        """
        return f'Книга "{self.title}" написана {self.author}, содержит {self.pages} страниц.'

    def is_long(self, threshold: int = 300) -> bool:
        """
        Проверяет, является ли книга длинной.

        :param threshold: Пороговое значение количества страниц. По умолчанию 300.
        :return: True, если количество страниц больше порога, иначе False.

        Пример:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.is_long()
        True
        """
        return self.pages > threshold


class Car:
    def __init__(self, brand: str, model: str, fuel_level: float):
        """
        Конструктор класса Car.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param fuel_level: Уровень топлива в баке. Должен быть в диапазоне от 0 до 100.

        :raises ValueError: Если уровень топлива выходит за допустимые пределы.
        """
        if not 0 <= fuel_level <= 100:
            raise ValueError("Уровень топлива должен быть в диапазоне от 0 до 100.")
        self.brand = brand
        self.model = model
        self.fuel_level = fuel_level

    def refuel(self, amount: float) -> None:
        """
        Заправляет автомобиль на указанное количество процентов.

        :param amount: Количество процентов для заправки. Должно быть положительным числом.

        :raises ValueError: Если количество топлива для заправки отрицательное.

        Пример:
        >>> car = Car("Toyota", "Corolla", 50.0)
        >>> car.refuel(30)
        >>> car.fuel_level
        80.0
        """
        if amount < 0:
            raise ValueError("Количество топлива для заправки должно быть положительным.")
        self.fuel_level = min(self.fuel_level + amount, 100)

    def can_drive(self, distance: float, fuel_consumption: float = 7.5) -> bool:
        """
        Проверяет, может ли автомобиль проехать указанное расстояние.

        :param distance: Расстояние в километрах.
        :param fuel_consumption: Расход топлива на 100 км. По умолчанию 7.5 л/100 км.
        :return: True, если топлива достаточно, иначе False.

        Пример:
        >>> car = Car("Toyota", "Corolla", 50.0)
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
        >>> account = Bank_Account("John Doe", 100.0)
        >>> account.deposit(50)
        >>> account.balance
        150.0
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
        >>> account = Bank_Account("John Doe", 100.0)
        >>> account.withdraw(30)
        30
        >>> account.balance
        70.0
        """
        if amount < 0:
            raise ValueError("Сумма для снятия должна быть положительной.")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете.")
        self.balance -= amount
        return amount


if __name__ == "__main__":
    doctest.testmod()
