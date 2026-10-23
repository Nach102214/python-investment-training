# Задача 1.40.
# Условие
    # Составить программу расчета значения функций:
    # x=(2/(a**2+25))+b / sqrt(b)+((a+b)+2)

import math


while True:
    a, b = map(float, input("Введите значения 'a' и 'b' через пробел: ").split())
    if b < 0:
        print("Ошибка: b должно быть >= 0 (в формуле есть sqrt(b))")
        continue
    else:
        numerator = (2 / (a ** 2 + 25)) + b
        denominator = math.sqrt(b) + ((a + b) + 2)
        x = numerator / denominator
        break

print(f"\nПри a = {a}, b = {b} x = {x}")
