# Скрипт для расчёта прибыли
# Дата: 22.09.2026 

ticker = "SBER"
buy_price = 250.50     # Цена покупки
sell_price = 245.75    # Цена продажи
quantity = 100         # Количество акций

# Расчёт
profit = (sell_price - buy_price) * quantity
profit_percent = (sell_price / buy_price - 1) * 100

# Вывод
print(f"=== Сделка по {ticker} ===")
print(f"Куплено: {quantity} шт. по {buy_price:.2f} руб.")
print(f"Продано: {quantity} шт. по {sell_price:.2f} руб.")
print(f"Прибыль: {profit:.2f} руб.")
print(f"Доходность: {profit_percent:.2f}%")
