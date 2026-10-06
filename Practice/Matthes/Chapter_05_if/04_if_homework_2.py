# Глава 5. Оператор if — домашнее задание 2
# Дата: (напиши дату)

# === Задача 1: Классификация акций по цене ===
prices = [150.50, 850.00, 1200.00, 15000.00, 300.00, 5000.00]

for price in prices:
    if price < 500:
        category = "Дешёвая"
    elif price < 1000:
        category = "Средняя"
    elif price < 5000:
        category = "Дорогая"
    else:
        category = "Премиум"
    print(f"{price:>8.2f} руб. - {category}")

# === Задача 2: Проверка портфеля на пустоту ===
portfolio = ["SBER", "GAZP", "LKOH"]

if portfolio:
    print(f"\nВ портфеле - {len(portfolio)} акций:")
    for stock in portfolio:
        print(f"  {stock}")
else:
    print("\nПортфель пуст. Добавь акции!")

# === Задача 3: Проверка нескольких запросов ===
wanted = ["SBER", "AAPL", "GAZP", "TSLA", "LKOH"]
allowed = ["SBER", "GAZP", "LKOH", "GMKN"]
quantity_purchased = 0

print()
for stock in wanted:
    if stock in allowed:
        print(f"Покупаем {stock}.")
        quantity_purchased += 1
    else:
        print(f"{stock} недоступна.")
print(f"Количество купленных акций - {quantity_purchased}")

# === Задача 4: Калькулятор скидки ===
amount = 100_001

if amount >= 100_000:
    discount = 0.10
elif amount >= 50_000:
    discount = 0.07
elif amount >= 10_000:
    discount = 0.05
else:
    discount = 0.0

final = amount * (1 - discount)

print(f"\nСумма: {amount:_.2f} руб.")
print(f"Скидка: {discount * 100:.0f}%")
print(f"Итог: {final:_.2f} руб.")
