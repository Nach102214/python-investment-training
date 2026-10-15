# Задача:
# Реализовать программу, которая считает сумму цифр натурального числа
# через while n > 0 — цикл с предусловием:

n = int(input("Введите натуральное число: "))
original = n  # сохраним для вывода
sum_of_digits = 0

while n > 0:
    last_digit = n % 10
    sum_of_digits += last_digit
    n = n // 10  # отбрасываем последнюю цифру

print(f"Сумма цифр числа {original} = {sum_of_digits}")
