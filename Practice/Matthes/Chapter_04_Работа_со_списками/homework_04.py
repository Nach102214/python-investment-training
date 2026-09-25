# Глава 4. Срезы списков
# Дата: 2026-09-25
# Цель: Научиться работать со срезами, zip и копированием списков

# 1. Создали два списка — тикеры и цены
tickers = ["SBER", "GAZP", "LKOH", "GMKN", "ROSN", "NVTK", "ALRS"]
prices = [250.50, 180.20, 4500.00, 12000.00, 550.75, 1192.80, 19.59]

print("=== Анализ портфеля ===")

# 2. Первые три элемента через срез
print(f"Первые три тикера: {tickers[:3]}")
print(f"Первые три цены: {prices[:3]}")

# 3. Последние два элемента через срез
print(f"\nДва последних тикера: {tickers[-2:]}")
print(f"Цены двух последних акций: {prices[-2:]}")

# 4. Элементы с шагом 2
print(f"\nКаждый второй тикер (индексы 0, 2, 4, 6): {tickers[::2]}")
print(f"Каждая вторая цена (индексы 0, 2, 4, 6): {prices[::2]}")

# 5. Топ-3 самых дорогих акций через zip + sorted + срез
pairs = list(zip(prices, tickers))   # сначала цена, потом тикер
pairs_sorted = sorted(pairs, reverse=True)  # по цене, от дорогих к дешёвым
top_3 = pairs_sorted[:3]

print("\nТоп-3 самых дорогих акций:")
for price, ticker in top_3:
    print(f"  {ticker}: {price:.2f} руб.")

# 6. Копия списка через [:], изменяем копию, доказываем, что оригинал не изменился
tickers_copy = tickers[:]
prices_copy = prices[:]

tickers_copy.append("NEW")
prices_copy.append(100.00)

print(f"\nОригинал тикеров: {tickers}")
print(f"Копия тикеров: {tickers_copy}")
print(f"Оригинал не изменился: {'NEW' not in tickers}")

print(f"\nОригинал цен: {prices}")
print(f"Копия цен: {prices_copy}")
print(f"Оригинал не изменился: {100.00 not in prices}")
