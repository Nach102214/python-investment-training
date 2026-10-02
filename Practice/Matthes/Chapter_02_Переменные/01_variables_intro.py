# Глава 2. Переменные
# Дата: 22.09.2026 
# Цель: Научиться работать с переменными и числами

# Переменная для цены акции
sber_price = 250.50

# Переменная для количества акций
sber_quantity = 100

# Переменная для тикера
sber_ticker = "SBER"

# Стоимость позиции:
total_cost = sber_price * sber_quantity

# Выводим значения
print(sber_price)
print(sber_quantity)
print(sber_ticker)
print(total_cost)

# f-строки — красивый вывод
ticker = "SBER"
price = 250.50
quantity = 100
total = price * quantity

# Плохо (так делать не надо)
print("Акция: " + ticker + ", цена: " + str(price))

# Хорошо (f-строка)
print(f"Акция: {ticker}, цена: {price}, стоимость: {total}")

