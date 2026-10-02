# Глава 4. Кортежи — домашнее задание
# Дата: 02.10.2026

# Задача 1: Размер окна
print("=== Задача 1: Размер окна ===")
window_size = (1200, 800)
width, height = window_size
print(f"Ширина: {width}, Высота: {height}")

# Задача 2: Портфель из кортежей
print("\n=== Задача 2: Портфель ===")
stocks = [
    ("SBER", 250.50, 100),
    ("GAZP", 180.20, 50),
    ("LKOH", 4500.00, 10),
    ("GMKN", 12000.00, 5),
]

total_cost = 0
max_price = stocks[0][1]
max_ticker = stocks[0][0]

for ticker, price, quantity in stocks:
    cost = price * quantity
    total_cost += cost
    if price > max_price:
        max_price = price
        max_ticker = ticker
    print(f"  {ticker}: {quantity} шт. по {price:.2f} руб. = {cost:.2f} руб.")

print(f"\nОбщая стоимость: {total_cost:.2f} руб.")
print(f"Самая дорогая акция: {max_ticker} ({max_price:.2f} руб.)")

# Задача 3: == vs is
print("\n=== Задача 3: == vs is ===")
a = (1, 2, 3)
b = (1, 2, 3)
print(f"a == b: {a == b}")   # True (значения одинаковые)
print(f"a is b: {a is b}")   # ? — предскажи!

# Задача 4: Кортеж из одного элемента
print("\n=== Задача 4: Один элемент ===")
single = (42,)
not_single = (42)
print(f"type((42,)) = {type(single)}")
print(f"type((42))  = {type(not_single)}")
print("Вывод: (42,) — кортеж; (42) — просто число!")
