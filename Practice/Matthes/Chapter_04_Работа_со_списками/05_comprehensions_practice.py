# Для каждого цикла — напиши генератор.
# Запусти оба варианта (цикл и генератор).
# Сравни результаты через print(... == ...)

prices = [100, 250, 500, 750, 1000]

# 1. Обычный цикл
result_1 = []
for p in prices:
    result_1.append(p + 100)

result_1_gen = [p + 100 for p in prices]
print("Списки равны?", result_1 == result_1_gen)

# 2. С условием
result_2 = []
for p in prices:
    if p > 300:
        result_2.append(p)

result_2_gen = [p for p in prices if p > 300]
print("Списки равны?", result_2 == result_2_gen)


# 3. С преобразованием и условием
result_3 = []
for p in prices:
    if p < 500:
        result_3.append(p * 2)

result_3_1 = [p *2 for p in prices if p < 500]
print("Списки равны?", result_3 == result_3_1)


# 4. Со строками
result_4 = []
for p in prices:
    result_4.append(f"{p} руб.")

result_4_1 = [f"{p} руб." for p in prices]
print("Списки равны?", result_4 == result_4_1)

# 5. С тернарным условием
result_5 = []
for p in prices:
    if p > 500:
        result_5.append("дорого")
    else:
        result_5.append("дёшево")

result_5_1 = ["дорого"if p > 500  else "дёшево" for p in prices]
print("Списки равны?", result_5 == result_5_1)


# Список прибыли по каждой акции (прибыль = (sell - buy) * qty).
# Список тикеров, по которым прибыль положительная (прибыльные сделки).
# Список тикеров, по которым прибыль отрицательная (убыточные).
# Общая прибыль (через sum()).

tickers = ["SBER", "GAZP", "LKOH", "GMKN", "ROSN"]
buy_prices = [250.00, 180.00, 4500.00, 12000.00, 550.00]
sell_prices = [260.50, 175.20, 4600.00, 11800.00, 560.75]
quantities = [100, 50, 10, 5, 20]


profit_list = [
        f"{ticker}: {(sell - buy) * qty:+.2f}" 
        for ticker, sell, buy, qty in zip(tickers, sell_prices, buy_prices, quantities)
        ]
print("\nСписок прибыли по каждой акции:")
print(profit_list)

profitable_tickers = [
        ticker for ticker, sell, buy in zip(tickers, sell_prices, buy_prices) if sell > buy
        ]
print("\nСписок тикеров, по которым прибыль положительная:")
print(profitable_tickers)


losing_tickers = [
        ticker for ticker, sell, buy in zip(tickers, sell_prices, buy_prices) if sell < buy
        ]
print("\nСписок тикеров, по которым прибыль отрицательная:")
print(losing_tickers)

total_profit = sum(
        (sell - buy) * qty for sell, buy, qty in zip(sell_prices, buy_prices, quantities)
        )
print("\nОбщая прибыль:")
print(f"{total_profit:+.2f}")




















