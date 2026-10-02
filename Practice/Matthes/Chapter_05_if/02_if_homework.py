# Задача 1: Категория счёта
# Есть переменная balance. Определи:
#     Если balance >= 1_000_000 → "Премиум"
#     Если balance >= 100_000 → "Стандарт"
#     Если balance >= 10_000 → "Базовый"
#     Иначе → "Минимальный"

balance = 101111

print("Категория счёта -> ", end="")
if balance >= 1_000_000:
    print("Премиум")
elif balance >= 100_000:
    print("Стандарт")
elif balance >= 10_000:
    print("Базовый")
else:
    print("Минимальный")


# Задача 2: Проверка портфеля
# Есть список tickers из 5 акций. Проверь:
#     Есть ли "SBER" в портфеле? Если да — выведи "Сбер есть в портфеле".
#     Есть ли "AAPL"? Если нет — выведи "Apple отсутствует в портфеле".

portfolio = ["SBER", "GAZP", "LKOH", "GMKN", "ROSN"]

if "SBER" in portfolio:
    print("\nСбер есть в портфеле")
if "AAPL" not in portfolio:
    print("\nApple отсутствует в портфеле")

# Задача 3: Решение о покупке
# Есть переменные:
#     price — цена акции.
#     pe_ratio — коэффициент P/E (соотношение цена/прибыль).
#     dividend_yield — дивидендная доходность.
# Правила покупки:
#     Если price < 1000 и pe_ratio < 15 — покупаем.
#     Если dividend_yield > 8 — покупаем (даже если дорого).
#     Иначе — не покупаем.
# Выведи результат.

price = 1_550
pe_ratio = 14
dividend_yield = 7

if price < 1000 and pe_ratio < 15 or dividend_yield > 8:
    print("\nПокупаем")
else:
    print("\nНе покупаем")

# Задача 4: Проверка вхождения
# Есть строка email = "user@example.com". Проверь:
#     Содержит ли она символ @?
#     Заканчивается ли на .com?
#     Заканчивается ли на .ru?

email = "user@example.com"

print()
if "@" in email:
    print("Email содержит символ @")
else:
    print("Email не содержит символ @")

if email.endswith(".com"):
    print("Email заканчивается на .com")

if email.endswith(".ru"):
    print("Email заканчивается на .ru")
else:
    print("Email не заканчивается на .ru")


# Вариант решения Учителя:
# Глава 5. Оператор if — домашнее задание

# === Задача 1: Категория счёта ===
balance = 101111

if balance >= 1_000_000:
    category = "Премиум"
elif balance >= 100_000:
    category = "Стандарт"
elif balance >= 10_000:
    category = "Базовый"
else:
    category = "Минимальный"

print(f"Категория счёта: {category}")

# === Задача 2: Проверка портфеля ===
portfolio = ["SBER", "GAZP", "LKOH", "GMKN", "ROSN"]

if "SBER" in portfolio:
    print("Сбер есть в портфеле")

if "AAPL" not in portfolio:
    print("Apple отсутствует в портфеле")

# === Задача 3: Решение о покупке ===
price = 1_550
pe_ratio = 14
dividend_yield = 7

# ВАЖНО: скобки для явного приоритета!
if (price < 1000 and pe_ratio < 15) or (dividend_yield > 8):
    print("Покупаем")
else:
    print("Не покупаем")

# Проверим разные сценарии
print("\n=== Тестирование правила ===")

# Сценарий 1: дешёвая и хорошая P/E
price, pe_ratio, dividend_yield = 500, 10, 3
decision = (price < 1000 and pe_ratio < 15) or (dividend_yield > 8)
print(
    f"price={price}, pe={pe_ratio}, div={dividend_yield} → {'Покупаем' if decision else 'Не покупаем'}"
)

# Сценарий 2: дорогая, но высокая дивидендная доходность
price, pe_ratio, dividend_yield = 5000, 20, 10
decision = (price < 1000 and pe_ratio < 15) or (dividend_yield > 8)
print(
    f"price={price}, pe={pe_ratio}, div={dividend_yield} → {'Покупаем' if decision else 'Не покупаем'}"
)

# Сценарий 3: дорогая и низкая дивидендная доходность
price, pe_ratio, dividend_yield = 5000, 20, 3
decision = (price < 1000 and pe_ratio < 15) or (dividend_yield > 8)
print(
    f"price={price}, pe={pe_ratio}, div={dividend_yield} → {'Покупаем' if decision else 'Не покупаем'}"
)

# === Задача 4: Проверка email ===
email = "user@example.com"

print(f"\nEmail: {email}")
print(f"Содержит @: {'@' in email}")
print(f"Заканчивается на .com: {email.endswith('.com')}")
print(f"Заканчивается на .ru: {email.endswith('.ru')}")
