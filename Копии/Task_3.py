 # 1. Используя цикл, выведи общее количество всех напитков за каждый день (сумма латте + капучино + эспрессо). 
 #    Формат вывода: "Пн: 45 напитков".
 #
 # 2. Используя цикл, посчитай и выведи общую выручку за все 3 дня, если цена: латте — 180 руб., 
 #    капучино — 160 руб., эспрессо — 120 руб. (подсказка: создай словарь с ценами prices = {"latte": 180, ...}).
 #
 # 3. (Сложное) Найди день с максимальной выручкой и выведи его название.

sales_data = [
    {"day": "Пн", "latte": 15, "cappuccino": 22, "espresso": 8},
    {"day": "Вт", "latte": 18, "cappuccino": 20, "espresso": 10},
    {"day": "Ср", "latte": 20, "cappuccino": 25, "espresso": 12}
]

print("Общее количество напитков за каждый день: ")
print()

for day_data in sales_data:
    total_quantity = 0
    for key, value in day_data.items():
        if key != 'day':
            total_quantity += value
    print(f"{day_data['day']}: {total_quantity} напитков")
print()

prices = {"latte": 180, "cappuccino": 160, "espresso": 120}

total_revenue = 0
daily_revenues = {}

for day_data in sales_data:
    day_name = day_data["day"]
    day_revenue = 0
    for drink, quantity in day_data.items():
        if drink != 'day':
            day_revenue += quantity * prices[drink]
    total_revenue += day_revenue
    daily_revenues[day_name] = day_revenue  # Записываем итог за день

# 2. Находим день с максимальной выручкой
best_day = max(daily_revenues, key=daily_revenues.get)
max_revenue = daily_revenues[best_day]

print("=== Статистика ===")
print()
print(f"Общая выручка за все 3 дня: {format(total_revenue, ',').replace(',', ' ')} руб.")
print(f"День с максимальной выручкой: {best_day} {format(max_revenue, ',').replace(',', ' ')}")

