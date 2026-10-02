# Напиши программу, которая:
#     Создаёт переменные для трёх акций (тикер, цена, количество).
#     Считает стоимость каждой позиции.
#     Считает общую стоимость портфеля.
#     Выводит красиво отформатированный отчёт.

ticker_sber, ticker_gazp, ticker_lkoh = "SBER", "GAZP", "LKOH"
price_sber, price_gazp, price_lkoh = 250.50, 180.2, 4500
quantity_sber, quantity_gazp, quantity_lkoh = 100, 50, 10

# Считаем стоимость каждой позиции:
total_cost_sber = price_sber * quantity_sber
total_cost_gazp = price_gazp * quantity_gazp
total_cost_lkoh = price_lkoh * quantity_lkoh
total_cost = total_cost_sber + total_cost_gazp + total_cost_lkoh

# Вывод результатов:
print("=== Мой портфель ===")
print(f"{ticker_sber}: {quantity_sber} шт. по {price_sber:.2f} руб. = {total_cost_sber:.2f} руб.")
print(f"{ticker_gazp}: {quantity_gazp} шт. по {price_gazp:.2f} руб. = {total_cost_gazp:.2f} руб.")
print(f"{ticker_lkoh}: {quantity_lkoh} шт. по {price_lkoh:.2f} руб. = {total_cost_lkoh:.2f} руб.")
print("-----------------------------")
print(f"Итого: {total_cost:.2f} руб.")

