# Глава 4. Генераторы списков (list comprehensions)
# Дата: 25.09.2026 
# Цель: Научиться создавать списки в одну строку

# Исходные данные
prices = [250.50, 180.20, 4500.00, 12000.00, 550.75]
tickers = ["SBER", "GAZP", "LKOH", "GMKN", "ROSN"]

# 1. Удвоить все цены — обычный цикл
doubled_old = []
for price in prices:
    doubled_old.append(price * 2)
print("Удвоенные (цикл):", doubled_old)

# 2. То же самое через генератор
doubled_new = [price * 2 for price in prices]
print("Удвоенные (генератор):", doubled_new)

# 3. Проверим, что результаты совпадают
print("Результаты совпадают:", doubled_old == doubled_new)

# Только цены > 500 руб.
expensive_prices = [price for price in prices if price > 500]
print("Дорогие цены (> 500):", expensive_prices)

# Только тикеры, у которых цена > 500 руб.
expensive_tickers = [tickers[i] for i in range(len(prices)) if prices[i] > 500]
print("Дорогие тикеры:", expensive_tickers)

# Создать список строк вида "SBER: 250.50"
labels = [f"{ticker}: {price:.2f}" for ticker, price in zip(tickers, prices)]
print("Ярлыки:", labels)

# Все цены → строки с округлением до 2 знаков
prices_as_strings = [f"{p:.2f}" for p in prices]
print("Строки:", prices_as_strings)

# Все тикеры → нижний регистр
tickers_lower = [t.lower() for t in tickers]
print("Нижний регистр:", tickers_lower)

# Все цены → целые (отбрасываем копейки)
prices_int = [int(p) for p in prices]
print("Целые:", prices_int)

# Если цена > 500 → "дорогая", иначе → "дешёвая"
categories = ["дорогая" if p > 500 else "дешёвая" for p in prices]
print("Категории:", categories)

buy_prices =  [250.00, 180.00, 4500.00, 12000.00, 550.00]
sell_prices = [260.50, 175.20, 4600.00, 11800.00, 560.75]
quantities =  [100, 50, 10, 5, 20]

# Прибыль по каждой сделке
profits = [(sell - buy) * qty for sell, buy, qty in zip(sell_prices, buy_prices, quantities)]
print("Прибыль по сделкам:", profits)

# Общая прибыль
total_profit = sum(profits)
print(f"Общая прибыль: {total_profit:.2f} руб.")

# Только прибыльные сделки
profitable = [p for p in profits if p > 0]
print("Прибыльные сделки:", profitable)

# Только убыточные сделки
losing = [p for p in profits if p < 0]
print("Убыточные сделки:", losing)

















































