# Создай список из 6 тикеров и 6 цен.
# Создай генератор, который:
#     Умножает каждую цену на 1.1 (учёт инфляции).
# Создай генератор, который:
#     Оставляет только тикеры с ценой > 1000 руб.
# Создай генератор, который:
#     Формирует список строк вида "SBER: дорогая" или "SBER: дешёвая" (порог 1000 руб.).
# Создай генератор, который:
#     Возвращает список квадратных корней из цен (price ** 0.5).
# Посчитай сумму всех цен через sum() — функция работает со списками.
#
# Выведи всё через print()

# 1. Создали два списка — тикеры и цены
tickers = ["SBER", "GAZP", "LKOH", "GMKN", "ROSN", "NVTK"]
prices = [250.50, 180.20, 4500.00, 12000.00, 550.75, 1192.80]

prices_inflation = [f"{price * 1.1:.2f}" for price in prices]

expensive_tickers = [tickers[i] for i in range(len(prices)) if prices[i] > 1000]

categories = [f"{ticker}: {'дорогая' if price > 1000 else 'дешёвая'}" for ticker, price in zip(tickers, prices)] 

square_roots_of_prices = [round(price ** 0.5, 2) for price in prices]

sum_prices = sum(prices)

# Вывод результатов:
print("=== Анализ с инфляцией ===")
print(f"Цены с инфляцией: {prices_inflation}")
print(f"Дорогие тикеры (>1000): {expensive_tickers}")
print(f"Категории: {categories}")
print(f"Квадратные корни: {square_roots_of_prices}")
print(f"Сумма всех цен: {sum_prices} руб.")



















