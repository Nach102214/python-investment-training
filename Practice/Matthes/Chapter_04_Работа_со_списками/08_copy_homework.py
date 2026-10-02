# Задача:
#     Создай список portfolio из 4 словарей (тикер, цена, количество). Пока словари — это просто литералы; мы разберём их в Главе 6.
#     Создай копию этого портфеля через copy.deepcopy().
#     В копии измени цену одной акции и добавь новую акцию.
#     Выведи оба портфеля, доказывая, что оригинал не изменился.
import copy

portfolio = [
    {"ticker": "SBER", "price": 250.50, "quantity": 100},
    {"ticker": "GAZP", "price": 180.20, "quantity": 50},
    {"ticker": "LKOH", "price": 4500.00, "quantity": 10},
    {"ticker": "GMKN", "price": 12000.00, "quantity": 5},
]
temp_portfolio = copy.deepcopy(portfolio) 
temp_portfolio[0]["price"] = 280.55
temp_portfolio.append({"ticker": "NORN", "price": 1250.50, "quantity": 10})

print("Оригинальный портфель:")
print(*(data for data in portfolio), sep='\n')
print("\nИзменённый портфель:")
print(*(data for data in temp_portfolio), sep='\n')

# Можно было без "data for data in portfolio" Потому что portfolio уже итерируемый объект, и * его распакует напрямую:
print()
print(*portfolio, sep='\n')

# Выполнил учитель:
# Глава 4. Копирование — глубокое
# Цель: понять разницу между ссылкой и копией

import copy

portfolio = [
    {"ticker": "SBER", "price": 250.50, "quantity": 100},
    {"ticker": "GAZP", "price": 180.20, "quantity": 50},
    {"ticker": "LKOH", "price": 4500.00, "quantity": 10},
    {"ticker": "GMKN", "price": 12000.00, "quantity": 5},
]

# Глубокая копия
temp_portfolio = copy.deepcopy(portfolio)

# Изменяем копию
temp_portfolio[0]["price"] = 280.55
temp_portfolio.append({"ticker": "NORN", "price": 1250.50, "quantity": 10})

# Вывод оригинала
print("Оригинальный портфель:")
for stock in portfolio:
    print(f"  {stock['ticker']}: {stock['quantity']} шт. по {stock['price']:.2f} руб.")

# Вывод копии
print("\nИзменённый портфель (копия):")
for stock in temp_portfolio:
    print(f"  {stock['ticker']}: {stock['quantity']} шт. по {stock['price']:.2f} руб.")

# Доказательство, что оригинал не изменился
print("\n=== Доказательство ===")
print(f"Оригинал содержит 4 акции: {len(portfolio) == 4}")
print(f"Цена SBER в оригинале не изменилась: {portfolio[0]['price'] == 250.50}")
print(f"NORN есть только в копии: {any(s['ticker'] == 'NORN' for s in temp_portfolio)}")













