# Задача:
#     Дано натуральное число n. Выведите все его делители в порядке возрастания.
#
# Идея:
#     Делитель — это число, на которое n делится без остатка (n % d == 0).
#     Перебираем d от 1 до n.
#     Если n % d == 0 — добавляем d в список.
#
# Пример: для n=12 → делители: 1, 2, 3, 4, 6, 12.

# Вариант А — простой (перебор до n)
n = int(input("Введите натуральное число (от 1 до бесконечности): "))

# Проверка ввода: цикл повторяется, пока n <= 0
while n <= 0:
    n = int(input("Число должно быть > 0. Попробуйте снова: "))

# Сохраняем оригинал ПОСЛЕ проверки — гарантированно корректное число
original = n
dividers = []

for d in range(1, n + 1):
    if n % d == 0:
        dividers.append(d)

print(f"\nСписок делителей для натурального числа {original}:")
print(dividers)



# Вариант Б — оптимизированный (перебор до √n) ⭐
n = int(input("Введите натуральное число: "))

while n <= 0:
    n = int(input("Число должно быть > 0. Попробуйте снова: "))
  
original = n
dividers = []

d = 1
while d * d <= n:   # пока d^2 <= n, то есть d <= sqrt(n)
    if n % d == 0:
        dividers.append(d)
        pair = n // d
        if pair != d:
            dividers.append(pair)
    d += 1

dividers.sort()   # сортируем, чтобы шли по возрастанию

print(f"\nДелители числа {original}:")
print(dividers)

# Проверка разницы в скорости исполнения кода (при n = 100_000):
import time

# Старый способ
start = time.time()
n_test = 100_000
dividers_old = []
for d in range(1, n_test + 1):
    if n_test % d == 0:
        dividers_old.append(d)
print(f"Перебор до n:      {time.time() - start:.4f} сек, делителей: {len(dividers_old)}")

# Новый способ
start = time.time()
dividers_new = []
d = 1
while d * d <= n_test:
    if n_test % d == 0:
        dividers_new.append(d)
        pair = n_test // d
        if pair != d:
            dividers_new.append(pair)
    d += 1
print(f"Перебор до sqrt(n): {time.time() - start:.4f} сек, делителей: {len(dividers_new)}")




