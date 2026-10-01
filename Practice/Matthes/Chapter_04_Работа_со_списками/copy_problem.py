# Глава 4. Копирование списков — проблема
# Дата: 01.10.2026 
# Цель: Понять, почему b = a НЕ создаёт копию

print("=== Эксперимент 1: b = a ===")
a = [1, 2, 3]
b = a               # b — это ВТОРОЙ ярлык на тот же список
print("a:", a)
print("b:", b)

b.append(4)         # изменяем через b
print("\nПосле b.append(4):")
print("a:", a)      # ← ИЗМЕНИЛСЯ!
print("b:", b)

# Проверим, что это один и тот же объект
print("\na is b:", a is b)  # True — один и тот же объект

print("\n=== Эксперимент 2: b = a[:] ===")
c = [1, 2, 3]
d = c[:]            # d — это КОПИЯ (срез создаёт новый список)
print("c:", c)
print("d:", d)

d.append(4)         # изменяем через d
print("\nПосле d.append(4):")
print("c:", c)      # ← НЕ изменился
print("d:", d)

print("\nc is d:", c is d)  # False — разные объекты

print("\n=== Сравнение == и is ===")
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(f"x == y: {x == y}")  # ? True
print(f"x is y: {x is y}")  # ? False
print(f"x == z: {x == z}")  # ? True
print(f"x is z: {x is z}")  # ? True


print("\n=== Три способа скопировать ===")
original = [1, 2, 3]

copy_1 = original[:]          # срез
copy_2 = list(original)       # list()
copy_3 = original.copy()      # .copy()

copy_1.append(100)
copy_2.append(200)
copy_3.append(300)

print("original:", original)  # [1, 2, 3] — не изменился
print("copy_1:", copy_1)      # [1, 2, 3, 100]
print("copy_2:", copy_2)      # [1, 2, 3, 200]
print("copy_3:", copy_3)      # [1, 2, 3, 300]

print("\n=== Поверхностная vs глубокая копия ===")
import copy

original = [[1, 2], [3, 4]]

shallow = original[:]              # поверхностная
deep = copy.deepcopy(original)     # глубокая

shallow[0].append(999)
print("original после shallow[0].append(999):", original)  # ИЗМЕНИЛСЯ!
print("shallow:", shallow)

# Сбрасываем original для чистого теста
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0].append(999)
print("\noriginal после deep[0].append(999):", original)   # НЕ изменился
print("deep:", deep)

# Копирование портфеля для анализа
tickers = ["SBER", "GAZP", "LKOH"]
prices = [250.50, 180.20, 4500.00]
quantities = [100, 50, 10]

# ❌ ОШИБКА: простое присваивание
# temp_tickers = tickers  ← изменит оригинал!

# ✅ ПРАВИЛЬНО: копии через срез
temp_tickers = tickers[:]
temp_prices = prices[:]
temp_quantities = quantities[:]

# Добавляем новую акцию ТОЛЬКО в temp
temp_tickers.append("GMKN")
temp_prices.append(12000.00)
temp_quantities.append(5)

# Проверяем
print("Оригинал (tickers):", tickers)            # 3 акции
print("Копия (temp_tickers):", temp_tickers)     # 4 акции
print("Оригинал не изменился:", len(tickers) == 3)






