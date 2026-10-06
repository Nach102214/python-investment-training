# Глава 5. Вложенные проверки и работа со списками
# Дата: 06.10.2026 
# Цель: Научиться комбинировать if с for, проверять вхождение, обрабатывать пустые списки

# === Часть 1: Вложенные if ===
print("=== Вложенные if ===")
cash = 50_000
price = 250.50
quantity = 100
has_stock = True 

if has_stock:
    print("Акция уже есть в портфеле — докупаем?")
    if cash >= price * quantity:
        print(f"  Хватает средств: {cash} >= {price * quantity:.2f}")
    else:
        print(f"  НЕ хватает: {cash} < {price * quantity:.2f}")
else:
    print("Акции нет в портфеле — начинаем с нуля")

# === Часть 2: if со списками ===
print("\n=== Обработка списка ===")
requested_stocks = ["SBER", "TSLA", "GAZP", "AAPL"]
available_stocks = ["SBER", "GAZP", "LKOH", "GMKN", "ROSN"]

for stock in requested_stocks:
    if stock in available_stocks:
        print(f"  {stock}: покупаем")
    else:
        print(f"  {stock}: недоступна")

# === Часть 3: Проверка на пустоту ===
print("\n=== Проверка на пустоту ===")
portfolio = []

if portfolio:
    print(f"В портфеле {len(portfolio)} акций")
else:
    print("Портфель пуст")

portfolio = ["SBER", "GAZP", "LKOH"]

if portfolio:
    print(f"В портфеле {len(portfolio)} акций:")
    for stock in portfolio:
        print(f"  {stock}")
else:
    print("Портфель пуст")

# Категория риска по волатильности
volatility = 25   # в процентах

if volatility < 10:
    risk = "Низкий"
elif volatility < 20:
    risk = "Средний"
elif volatility < 35:
    risk = "Высокий"
else:
    risk = "Очень высокий"

print(f"\nВолатильность: {volatility}%, риск: {risk}")

profit = 750_000

if profit <= 100_000:
    tax = 0
elif profit <= 500_000:
    tax = (profit - 100_000) * 0.13
elif profit <= 1_000_000:
    tax = 400_000 * 0.13 + (profit - 500_000) * 0.15
else:
    tax = 400_000 * 0.13 + 500_000 * 0.15 + (profit - 1_000_000) * 0.20

print(f"\nПрибыль: {profit:.2f} руб.")
print(f"Налог: {tax:.2f} руб.")
print(f"Чистая прибыль: {profit - tax:.2f} руб.")











