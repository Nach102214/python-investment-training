# **A1.** Создай переменные:
# - `ticker` = "SBER"
# - `price` = 250.75
# - `shares` = 100
# - `is_profitable` = True
#
# Выведи каждую через `print()`, а затем через `print(type(...))` для каждой.

ticker = "SBER"
price = 250.75
shares = 100
is_profitable = True

print(f"Переменная ticker = {ticker}, её тип: {type(ticker)}")
print(f"Переменная price = {price}, её тип: {type(price)}")
print(f"Переменная shares = {shares}, её тип: {type(shares)}")
print(f"Переменная is_profitable = {is_profitable}, её тип: {type(is_profitable)}")

# **A2.** Что выведет?
print()         # Пустая строка для отделения от предыдущего задания
a = 10
b = 3
print(f"{a / b:.4f}")    # Выведет 3.3333
print(a // b)   # Выведет 3 
print(a % b)    # Выведет 1

print()
print("--- Проверка типов результата ---")
print(f"{type(a / b) = }")
print(f"{type(a // b) = }")
print(f"{type(a % b) = }")
print(f"{10 / 2 = }")           # удивишься: 5.0, а не 5
print(f"{-10 % 3 = }")          # удивишься: 2, а не -1

# A3. Выведи int(3.99), int(-3.99), round(3.99), round(3.5), round(2.5). 
      # Сравни результаты. В комментарии объясни своими словами, чем int() отличается от round(). 
      # Обрати внимание на round(2.5) — он тебя удивит.
print()
print("--- Сравнение результатов округления ---")
print(f"При помощи 'int()': {int(3.99)}")
print(f"При помощи 'int()' отрицательное число: {int(-3.99)}")  # int() просто "отбрасывает" дробную часть и оставляет целую часть
print(f"При помощи 'round()': {round(3.99)}")                   # а round() именно округляет, при указании второго аргумента - с указанной точностью
print(f"При помощи 'round()': {round(-3.9987654321, 3)}")
print(f"При помощи 'round()': {round(3.5)}")
print(f"При помощи 'round()': {round(2.5)}")                    # Почему так??? Python использует правило «округления до ближайшего чётного»!!! Проверим:
print("\nПроверим, что 'round(6.5)' будет 6, а не 7:")
print(f"При помощи 'round()': {round(6.5)}")


# 🟡 B. Практика

# B1. Пользователь вводит цену акции (строка). Преобразуй её в float
#     и выведи "Цена: X руб.".
print("\n")
stock_price = float(input("Введите цену акции: "))
print(f"Цена: {stock_price} руб.")

# B2. Есть price = 99.99, shares = 50. Найди стоимость позиции.
print("\nСохрани в переменную position_value и выведи.")

price = 99.99
shares = 50

position_value = price * shares

print(f"Стоимость позиции: {position_value}")

# B3. 
print("\nПользователь вводит два числа (через input()).")
print("Выведи их сумму, разность, произведение, частное и остаток от деления.")

# Получаем ввод и сразу превращаем в числа
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

# Считаем все операции
summa = a + b
difference = a - b
product = a * b
quotient = a / b
remainder = a % b

# Выводим результаты
print(f"\nСумма: {summa}")
print(f"Разность: {difference}")
print(f"Произведение: {product}")
print(f"Частное: {quotient:.2f}")
print(f"Остаток от деления: {remainder}")

# B4. 💡 Алгоритмическая. 
print("\nПользователь вводит температуру в Цельсиях.")
print("Переведи в Фаренгейты (F = C * 9/5 + 32) и выведи.")

celsius = float(input("Введите температуру в градусах Цельсия: "))

fahrenheit = celsius * 9 / 5 + 32

# Вывод результата
print(f"\nВы ввели {celsius}, в Фаренгетах это {fahrenheit:.2f}")
 

# 🔴 C. Со звёздочкой

#C1. 
print("\nПользователь вводит сумму в рублях.") 
print("Выведи её в формате: '12 345.67 руб.' (с разделителем тысяч).") 

amount = "12345.67"
formatted = f"{float(amount):,.2f}".replace(',', ' ')

# Вывод результата
print(f"{formatted} руб.")

# C2. 
print('\nЕсть строка "100". Сделай из неё: ')
# число 100
# число 100.0
# и снова строку "100"
# Проверь типы через type().

s = "100"

# Строка → целое число
num_int = int(s)

# Строка → число с плавающей точкой (можно и из строки, и из int)
num_float = float(s)          # или float(num_int)

# Число обратно в строку
s_again = str(num_int)        # или str(num_float)

print(f"Строка: {s}, тип: {type(s)}")
print(f"Целое число: {num_int}, тип: {type(num_int)}")
print(f"Число с плавающей точкой: {num_float}, тип: {type(num_float)}")
print(f"Снова строка: {s_again}, тип: {type(s_again)}")

# C3. 💡 Пользователь вводит количество акций и цену.
print("\nВыведи прибыль, если известна цена покупки и цена продажи.")

# Запрс ввода от пользователя
quantity = int(input("Введите количество акций: "))
buy_price = float(input("Введите цену покупки одной акции: "))
sell_price = float(input("Введите цену продажи одной акции: "))

profit = (sell_price - buy_price) * quantity

# Выводим результат
print(f"Прибыль: {profit:.2f} руб.")















