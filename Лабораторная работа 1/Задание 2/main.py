from task_1 import Book, Car, Bank_Account

if __name__ == "__main__":

    # Проверка класса Book
    try:
        # Пытаемся создать книгу с некорректным количеством страниц
        invalid_book = Book("Invalid Book", "Author", -10)
    except ValueError as e:
        print(f"Ошибка: неправильные данные")

    # Проверка класса Car
    try:
        # Создаем автомобиль с корректными данными
        car = Car("Lada", "Largus", 50.0)
        # Пытаемся заправить автомобиль отрицательным количеством топлива
        car.refuel(-10)
    except ValueError as e:
        print(f"Ошибка: неправильные данные")

    # Проверка класса BankAccount
    try:
        # Создаем банковский счет с корректными данными
        account = Bank_Account("John Wick", 100.0)
        account.deposit(50)
        withdrawn_amount = account.withdraw(30)
        # Пытаемся снять отрицательную сумму
        account.withdraw(-10)
    except ValueError as e:
        print(f"Ошибка: неправильные данные")
    try:
        # Пытаемся снять сумму, превышающую баланс
        account.withdraw(200)
    except ValueError as e:
        pass
