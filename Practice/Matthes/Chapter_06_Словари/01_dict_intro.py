# Глава 6. Словари
# Дата: 06.10.2026 
# Цель: Научиться работать со словарями

# Шаг 1. Словарь для одной акции
stock = {
    "ticker": "SBER",
    "price": 250.50,
    "quantity": 100,
    "sector": "Финансы",
}

print("Акция:", stock)
print("Тикер:", stock["ticker"])
print("Цена:", stock["price"])
print("Количество:", stock["quantity"])
print("Сектор:", stock["sector"])

# Стоимость позиции
cost = stock["price"] * stock["quantity"]
print(f"\nСтоимость позиции: {cost:.2f} руб.")


stock = {"ticker": "SBER", "price": 250.50}

# Шаг 2. Добавление новой пары
stock["quantity"] = 100
stock["sector"] = "Финансы"

print(stock)
# {'ticker': 'SBER', 'price': 250.5, 'quantity': 100, 'sector': 'Финансы'}

# Шаг 3. Изменение значения
stock["price"] = 265.75
print(stock["price"])   # 265.75

# Шаг 4. Удаление пары
del stock["sector"]
print(stock)   # {'ticker': 'SBER', 'price': 265.75, 'quantity': 100}


# Шаг 5. Перебор словаря

#Способ 1: Перебор ключей
stock = {"ticker": "SBER", "price": 250.50, "quantity": 100}

for key in stock:
    print(f"{key}: {stock[key]}")

#Способ 2: Перебор пар (рекомендуется)

for key, value in stock.items():
    print(f"{key}: {value}")


# Шаг 6: Список словарей — портфель
# Это самый важный паттерн для инвестиций. Портфель — это список словарей, где каждый словарь — это одна акция.

portfolio = [
    {"ticker": "SBER", "price": 250.50, "quantity": 100},
    {"ticker": "GAZP", "price": 180.20, "quantity": 50},
    {"ticker": "LKOH", "price": 4500.00, "quantity": 10},
]

for stock in portfolio:
    ticker = stock["ticker"]
    price = stock["price"]
    quantity = stock["quantity"]
    cost = price * quantity
    print(f"{ticker}: {quantity} шт. по {price:.2f} руб. = {cost:.2f} руб.")

# Задание: добавь в портфель ещё две акции (GMKN, ROSN). Напиши общую стоимость портфеля через sum(...) и генератор.

portfolio = [
    {"ticker": "SBER", "price": 250.50, "quantity": 100},
    {"ticker": "GAZP", "price": 180.20, "quantity": 50},
    {"ticker": "LKOH", "price": 4500.00, "quantity": 10},
]
# Добавляем ещё две акции в портфель с помощью метода .append:

portfolio.append({"ticker": "GMKN", "price": 119.36, "quantity": 100})
portfolio.append({"ticker": "ROSN", "price": 345.50, "quantity": 50})

# Находим общую стоимость портфеля через sum() и генератор:

total_cost = sum(stock["price"] * stock["quantity"] for stock in portfolio)
print(f"\nОбщая стоимость портфеля - {total_cost:_.2f} руб.")


# Шаг 7: Вложенные словари
# Иногда нужно хранить много данных об одном объекте. Тогда используют вложенные словари.

portfolio = {
    "SBER": {"price": 250.50, "quantity": 100, "sector": "Финансы"},
    "GAZP": {"price": 180.20, "quantity": 50, "sector": "Нефть и газ"},
    "LKOH": {"price": 4500.00, "quantity": 10, "sector": "Нефть и газ"},
}

# Доступ к данным
print(f"SBER: {portfolio['SBER']['price']} руб.")
print(f"Сектор LKOH: {portfolio['LKOH']['sector']}")

# Перебор
for ticker, data in portfolio.items():
    price = data["price"]
    quantity = data["quantity"]
    cost = price * quantity
    print(f"{ticker}: {cost:.2f} руб.")

# Задание: создай словарь словарей для 5 акций. Выведи все тикеры и стоимость каждой позиции.

portfolio = {
    "SBER": {"price": 250.50, "quantity": 100, "sector": "Финансы"},
    "GAZP": {"price": 180.20, "quantity": 50, "sector": "Нефть и газ"},
    "LKOH": {"price": 4500.00, "quantity": 10, "sector": "Нефть и газ"},
}
portfolio["GMKN"] = {"price": 119.36, "quantity": 100, "sector": "Металлургия"}
portfolio["ROSN"] = {"price": 345.50, "quantity": 50, "sector": "Нефть и газ"}

for ticker, data in portfolio.items():
    position_cost = data["price"] * data["quantity"]
    print(f"Акция {ticker}, стоимость в портфеле: {position_cost:>8.2f} руб.")


# Шаг 8: Методы словаря
# Полезные методы:

stock = {"ticker": "SBER", "price": 250.50, "quantity": 100}

# Получить значение с дефолтом
value = stock.get("sector", "Не указан")
print(value)   # Не указан

# Получить все ключи
print(stock.keys())     # dict_keys(['ticker', 'price', 'quantity'])

# Получить все значения
print(stock.values())   # dict_values(['SBER', 250.5, 100])

# Получить все пары
print(stock.items())    # dict_items([('ticker', 'SBER'), ('price', 250.5), ('quantity', 100)])

# Проверить наличие ключа
print("ticker" in stock)  # True
print("sector" in stock)  # False

# Главный метод — .get() — безопасный доступ. Если ключа нет — вернёт дефолт вместо ошибки.
# Пример: если у одной акции нет поля sector, а у другой есть:

stock = {"ticker": "SBER", "price": 250.50}

# ❌ Ошибка, если ключа нет
# print(stock["sector"])   # KeyError

# ✅ Безопасно
sector = stock.get("sector", "Не указан")
print(sector)   # Не указан

# Это критически важный метод. В реальных данных всегда есть пропуски.


# Шаг 9: Практический пример — анализ портфеля

portfolio = [
    {"ticker": "SBER", "price": 250.50, "quantity": 100, "sector": "Финансы"},
    {"ticker": "GAZP", "price": 180.20, "quantity": 50, "sector": "Нефть и газ"},
    {"ticker": "LKOH", "price": 4500.00, "quantity": 10, "sector": "Нефть и газ"},
    {"ticker": "GMKN", "price": 12000.00, "quantity": 5, "sector": "Металлургия"},
    {"ticker": "ROSN", "price": 550.75, "quantity": 20, "sector": "Нефть и газ"},
]

# Общая стоимость
total = sum(s["price"] * s["quantity"] for s in portfolio)
print(f"Общая стоимость портфеля: {total:.2f} руб.\n")

# Стоимость по секторам
sectors = {}
for stock in portfolio:
    sector = stock["sector"]
    cost = stock["price"] * stock["quantity"]
    if sector in sectors:
        sectors[sector] += cost
    else:
        sectors[sector] = cost

print("Стоимость по секторам:")
for sector, cost in sectors.items():
    percent = cost / total * 100
    print(f"  {sector}: {cost:.2f} руб. ({percent:.1f}%)")





















