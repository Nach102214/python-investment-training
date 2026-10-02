# reinforcement_of_the_material.py
# Повторение материала: списки, zip, sum, генераторы, поиск максимума

tickers = ["SBER", "GAZP", "LKOH", "GMKN", "ROSN"]
prices = [250.50, 180.20, 4500.00, 12000.00, 550.75]
quantities = [100, 50, 10, 5, 20]

# 1. Общая стоимость портфеля — через цикл
total_cost = 0
for price, quantity in zip(prices, quantities):
    total_cost += price * quantity

# 2. То же самое — через генератор (в одну строку)
total_cost_gen = sum(price * quantity for price, quantity in zip(prices, quantities))

# Проверяем, что результаты совпадают
print(f"Цикл и генератор совпадают: {total_cost == total_cost_gen}")

# 3. Ищем самую дорогую акцию
max_price = prices[0]
max_ticker = tickers[0]
for i in range(len(tickers)):
    if prices[i] > max_price:
        max_price = prices[i]
        max_ticker = tickers[i]

# 4. Выводим отчёт
print("\n=== Мой портфель ===")
for ticker, price, quantity in zip(tickers, prices, quantities):
    cost = price * quantity
    print(f"{ticker}: {quantity} шт. по {price:.2f} руб. = {cost:.2f} руб.")

print("-----------------------------")
print(f"Итого: {total_cost:_.2f} руб.")
print(f"\nСамая дорогая акция в портфеле — {max_ticker}, её цена {max_price:.2f} руб.")

# 5. Сортируем тикеры по алфавиту (не трогая оригинал)
sorted_tickers = sorted(tickers)
print(f"Отсортированный список тикеров: {sorted_tickers}")
