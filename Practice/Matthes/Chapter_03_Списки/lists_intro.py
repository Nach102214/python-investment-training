# Глава 3. Списки
# Дата: 23.09.2026 
# Цель: Научиться работать со списками

# Список тикеров акций
tickers = ["SBER", "GAZP", "LKOH", "GMKN", "ROSN"]

# Список цен (в том же порядке, что и тикеры)
prices = [250.50, 180.20, 4500.00, 12000.00, 550.75]

# Список количеств
quantities = [100, 50, 10, 5, 20]

# Выводим список целиком
print("Тикеры:", tickers)
print("Цены:", prices)
print("Количества:", quantities)

# Выводим длину списка (сколько элементов)
print("Всего акций в портфеле:", len(tickers))

# Первый элемент (индекс 0)
print(tickers[0])   # SBER

# Второй элемент (индекс 1)
print(tickers[1])   # GAZP

# Последний элемент (индекс -1)
print(tickers[-1])  # ROSN

# Предпоследний элемент (индекс -2)
print(tickers[-2])  # GMKN

# Перебор по элементам
for ticker in tickers:
    print(ticker)


# Но нам нужно три списка одновременно. Для этого используем индексы:
# Перебор по индексам
for i in range(len(tickers)):
    ticker = tickers[i]
    price = prices[i]
    quantity = quantities[i]
    cost = price * quantity
    print(f"{ticker}: {quantity} шт. по {price:.2f} руб. = {cost:.2f} руб.")

my_portfolio = []
my_portfolio.append("GAZP")
my_portfolio.append("NORN")
my_portfolio.append("SBER")
print(f"\nМой портфель: {my_portfolio}")

tickers = ["SBER", "GAZP", "LKOH", "GMKN", "ROSN"]

# Удалить по значению
tickers.remove("GAZP")
print("После remove:", tickers)

# Удалить по индексу через del
del tickers[0]  # удалить первый элемент (SBER)
print("После del:", tickers)

# Удалить последний элемент через pop
last = tickers.pop()
print("Удалён:", last)
print("После pop:", tickers)

# Шаг 8: Сортировка (sort, sorted)
prices = [250.50, 180.20, 4500.00, 12000.00, 550.75]

# Временная сортировка (оригинал не меняется)
print("Отсортированные:", sorted(prices))
print("Оригинал:", prices)

# Постоянная сортировка
prices.sort()
print("После sort:", prices)

# Обратная сортировка
prices.sort(reverse=True)
print("После sort(reverse=True):", prices)


