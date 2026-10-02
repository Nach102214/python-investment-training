# Глава 4. Кортежи (tuples)
# Дата: 02.10.2026
# Цель: Понять, что такое кортеж и когда его использовать

# 1. Создаём кортеж
dimensions = (200, 50)
print("Размеры:", dimensions)
print("Тип:", type(dimensions))

# 2. Доступ по индексу
print("\nПервая сторона:", dimensions[0])
print("Вторая сторона:", dimensions[1])
print("Последняя:", dimensions[-1])

# 3. Длина кортежа
print("\nКоличество элементов:", len(dimensions))

# 4. Попробуем изменить — НЕ РАБОТАЕТ!
try:
    dimensions[0] = 250
except TypeError as e:
    print(f"\nОшибка: {e}")

# 5. Перебор кортежа
print("\nПеребор:")
for dim in dimensions:
    print(f"  {dim}")

# 6. Распаковка
x, y = dimensions
print(f"\nРаспаковка: x = {x}, y = {y}")

# 7. Кортеж из одного элемента
not_a_tuple = (5)             # это int
real_tuple = (5,)             # это tuple
print(f"\n(5) — это {type(not_a_tuple)}")
print(f"(5,) — это {type(real_tuple)}")

# 8. Практический пример: топ-3 акции через кортежи
tickers = ["SBER", "GAZP", "LKOH", "GMKN", "ROSN"]
prices = [250.50, 180.20, 4500.00, 12000.00, 550.75]

pairs = list(zip(tickers, prices))
pairs_sorted = sorted(pairs, key=lambda p: p[1], reverse=True)
top_3 = pairs_sorted[:3]

print("\nТоп-3 самых дорогих:")
for ticker, price in top_3:
    print(f"  {ticker}: {price:.2f} руб.")
