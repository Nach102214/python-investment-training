# Глава 5. Оператор if
# Дата: 02.10.2026
# Цель: Научиться проверять условия

# Пример из инвестиций: прибыль по сделке
profit = 1050.50

# Проверка: прибыль положительная?
if profit > 0:
    print(f"Сделка прибыльная! Прибыль: {profit:.2f} руб.")

print("Проверка завершена.")

profit = -240.00  # убыток

if profit > 0:
    print(f"Сделка прибыльная! Прибыль: {profit:.2f} руб.")

print("Проверка завершена.")

profit = -240.00

if profit > 0:
    print(f"Прибыль: +{profit:.2f} руб.")
else:
    print(f"Убыток: {profit:.2f} руб.")

score = 88

if score >= 90:
    category = "отличник"
elif score >= 80:
    category = "хорошист"
elif score >= 60:
    category = "троечник"
else:
    category = "двоечник"

print(f"Балл: {score}, категория: {category}")

# Список тикеров
portfolio = ["SBER", "GAZP", "LKOH", "GMKN", "ROSN"]

# Проверка: есть ли SBER в портфеле?
if "SBER" in portfolio:
    print("SBER есть в портфеле!")

# Проверка: есть ли AAPL?
if "AAPL" not in portfolio:
    print("AAPL отсутствует в портфеле")

age = 19
citizen = True

if age >= 18 and citizen:
    print("Можно голосовать")
else:
    print("Нельзя голосовать")

# Задание: напиши проверку для инвестиций:
#     Купить акцию, если цена < 500 и риск < 5.
#     Не покупать, если цена > 10000 или риск > 8

price = 250.50
risk = 3

if price < 500 and risk < 5:
    print("Покупаем!")

if price > 10000 or risk > 8:
    print("Не покупаем!")
