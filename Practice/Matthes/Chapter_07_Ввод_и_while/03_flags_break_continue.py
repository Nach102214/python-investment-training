# Пример 1 — Флаг
#
# Программа, которая спрашивает города, пока пользователь не введёт quit. Используй флаг active:

prompt = "\nВведите город (или 'quit' для выхода): "
active = True

while active:
    city = input(prompt)
    if city == 'quit':
        active = False
    else:
        print(f"Я хотел бы посетить город {city.title()}!")


# Пример 2 — break
#
# То же самое, но через break:

prompt = "\nВведите город (или 'quit' для выхода): "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    print(f"Я хотел бы посетить город {city.title()}!")


# Пример 3 — continue
#
# Счётчик от 1 до 10, но выводит только нечётные числа:

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)































