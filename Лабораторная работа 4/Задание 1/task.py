class Vehicle:
    """
    Базовый класс для транспортных средств.

    Атрибуты:
        brand (str): Марка транспортного средства.
        model (str): Модель транспортного средства.
        year (int): Год выпуска.
        mileage (float): Пробег в километрах.
    """

    def __init__(self, brand: str, model: str, year: int, mileage: float):
        """
        Инициализация транспортного средства.

        Аргументы:
            brand (str): Марка транспортного средства.
            model (str): Модель транспортного средства.
            year (int): Год выпуска.
            mileage (float): Пробег в километрах.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def __str__(self):
        """Строковое представление транспортного средства."""
        return f"{self.brand} {self.model} ({self.year}), пробег: {self.mileage} км"

    def __repr__(self):
        """Строковое представление для отладки."""
        return f"Vehicle(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, mileage={self.mileage!r})"

    def drive(self, distance: float) -> None:
        """
        Увеличивает пробег транспортного средства.

        Аргументы:
            distance (float): Расстояние в километрах.
        """
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным числом")
        self.mileage += distance
        print(f"Пробег увеличен на {distance} км. Текущий пробег: {self.mileage} км")


class Car(Vehicle):
    """
    Класс легкового автомобиля. Наследует от Vehicle.

    Дополнительные атрибуты:
        fuel_type (str): Тип топлива (бензин, дизель, электроэнергия).
        owner (str): Владелец автомобиля.
    """

    def __init__(self, brand: str, model: str, year: int, mileage: float, fuel_type: str, owner: str):
        """
        Инициализация легкового автомобиля.

        Аргументы:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска.
            mileage (float): Пробег в километрах.
            fuel_type (str): Тип топлива.
            owner (str): Владелец автомобиля.
        """
        super().__init__(brand, model, year, mileage)
        self.fuel_type = fuel_type
        self.owner = owner

    def __str__(self):
        """Строковое представление легкового автомобиля."""
        return f"{self.brand} {self.model} ({self.year}), топливо: {self.fuel_type}, пробег: {self.mileage} км"

    def __repr__(self):
        """Строковое представление для отладки."""
        return (
            f"Car(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, "
            f"mileage={self.mileage!r}, fuel_type={self.fuel_type!r}, owner={self._owner!r})"
        )

    @property
    def owner(self) -> str:
        """Возвращает владельца автомобиля."""
        return self.owner

    @owner.setter
    def owner(self, new_owner: str) -> None:
        """
        Устанавливает нового владельца автомобиля.

        Аргументы:
            new_owner (str): Имя нового владельца.
        """
        if not new_owner:
            raise ValueError("Имя владельца не может быть пустым")
        self.owner = new_owner

    def honk(self) -> None:
        """Издает звук сигнала."""
        print(f"{self.brand} {self.model} говорит Буп-Буп!")
