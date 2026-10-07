# Задача 1: Информация о человеке
#     Создай словарь person с полями: first_name, last_name, age, city.
#     Выведи каждое поле отдельно.
#     Добавь поле email.
#     Измени age на новое значение.
#     Выведи словарь целиком.

person = {"first_name": "Aleks", "last_name": "Ivanov", "age": 33, "city": "Chita"}

# Выведем каждое поле отдельно:
for key, value in person.items():
    print(f"{key}: {value}")

# Добаим новое поле email:
person["email"] = "ivanov@mail.ru"

# Изменим age на новое значение:
person["age"] = 35

# Выведем словарь каждое поле отдельно и, проверочно, целиком:
print(f"\nИмя: {person['first_name']}")
print(f"Фамилия: {person['last_name']}")
print(f"Возраст: {person['age']}")
print(f"Город: {person['city']}")
print(f"Электронный адрес: {person['email']}")
print(f"Отладка: {person}")


# Задача 2: Любимые числа
#     Создай словарь favorite_numbers с 3 людьми и их любимыми числами.
#     Выведи для каждого человека: "У {name} любимое число — {number}".

favorite_numbers = {"Sergey": 777, "Ivan": 21, "Aleks": 12}
for name, number in favorite_numbers.items():
    print(f"У {name} любимое число - {number}.")


# Задача 3: Портфель — список словарей
#     Создай список из 5 акций (словари с ticker, price, quantity, sector).
#     Выведи каждую акцию в формате: "SBER: 100 шт. по 250.50 руб. = 25050.00 руб.".
#     Посчитай общую стоимость портфеля.

portfolio = [
    {"ticker": "SBER", "price": 250.50, "quantity": 100, "sector": "Финансы"},
    {"ticker": "GAZP", "price": 180.20, "quantity": 50, "sector": "Нефть и газ"},
    {"ticker": "LKOH", "price": 4500.00, "quantity": 10, "sector": "Нефть и газ"},
    {"ticker": "GMKN", "price": 12000.00, "quantity": 5, "sector": "Металлургия"},
    {"ticker": "ROSN", "price": 550.75, "quantity": 20, "sector": "Нефть и газ"},
]
total_cost = 0

for data in portfolio:
    cost = data["price"] * data["quantity"]
    total_cost += cost
    print(f"{data['ticker']}: {data['quantity']} шт. по {data['price']:.2f} руб. = {cost:_.2f} руб.")
print(f"Общая стоимость портфеля: {total_cost:_.2f} руб.")


# Задача 4: Группировка по секторам
#     Используя портфель из Задачи 3, сгруппируй стоимость по секторам.
#     Выведи результат:
# Финансы: 25050.00 руб.
# Нефть и газ: 56025.00 руб.
# Металлургия: 60000.00 руб.

sectors = {}
for stock in portfolio:
    sector = stock["sector"]
    cost = stock["price"] * stock["quantity"]
    if sector in sectors:
        sectors[sector] += cost
    else:
        sectors[sector] = cost

for sector, cost in sectors.items():
    print(f"{sector}: {cost:_.2f} руб.")


# Задача 5: Вложенные словари
#     Перепиши портфель из Задачи 3 как словарь словарей, где ключ — тикер.
#     Найди стоимость акции "SBER" через portfolio["SBER"]["price"] * portfolio["SBER"]["quantity"].


portfolio = {
        "SBER": {"price": 250.50, "quantity": 100, "sector": "Финансы"},
     "GAZP": {"price": 180.20, "quantity": 50, "sector": "Нефть и газ"},
     "LKOH": {"price": 4500.00, "quantity": 10, "sector": "Нефть и газ"},
     "GMKN": {"price": 12000.00, "quantity": 5, "sector": "Металлургия"},
     "ROSN": {"price": 550.75, "quantity": 20, "sector": "Нефть и газ"},
}

total_cost_SBER = portfolio["SBER"]["price"] * portfolio["SBER"]["quantity"]
print(f"\nСтоимость акций SBER в портфеле: {total_cost_SBER:_.2f} руб.")













