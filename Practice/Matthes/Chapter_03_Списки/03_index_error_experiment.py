# Эксперимент: что произойдёт?

tickers = ["SBER", "GAZP", "LKOH"]

# 1. Что выведет это?
print(tickers[0])

# 2. А это?
print(tickers[-1])

# 3. Что если попробовать индекс 10?
print(tickers[10])  # Раскомментируй и посмотри ошибку

# 4. Что выведет это?
tickers.append("GMKN")
print(tickers)

# 5. Что если удалить?
tickers.remove("GAZP")
print(tickers)

# 6. Что выведет sorted?
print(sorted(tickers))

# 7. А что вернёт len?
print(len(tickers))
