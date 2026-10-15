# Цикл с параметром (со счётчиком)
# Задача:
# Вывести столбиком числа от 10 до 20 с шагом 1

for i in range(10, 21):
    print(i)


# Попробуем с помощью for решить следующую задачу:
#     Дано натуральное число n.
#     Требуется найти его сумму цифр.

n = 30625
remember = n
sum_num = 0

for i in range(0, len(str(n))):
    res = n % 10
    sum_num += res
    n //= 10
print(f"\nСумма цифр числа {remember} равна {sum_num}")

# Более красивый способ:
#     превращаем число в строку, берем каждую цифру-символ, превращаем её обратно 
#     в число через int() и складываем:

n = 30625
sum_num = 0

for number in str(n):
    sum_num += int(number)

print(f"\nСумма цифр числа {n} равна {sum_num}")

# Эта же задача через while:

n = 30625
sum_num = 0
remember = n

while n > 0:
    sum_num += n % 10
    n //= 10

print(f"\nСумма цифр числа {remember} равна {sum_num}")


import time

n_big = 12345678901234567890

# Способ 1: for + str
start = time.perf_counter()
for _ in range(100_000):
    s = 0
    for ch in str(n_big):
        s += int(ch)
print(f"for + str:      {time.perf_counter() - start:.3f} сек")

# Способ 2: while
start = time.perf_counter()
for _ in range(100_000):
    x = n_big
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
print(f"while:          {time.perf_counter() - start:.3f} сек")

# Способ 3: sum(map(int, str(n)))
start = time.perf_counter()
for _ in range(100_000):
    s = sum(map(int, str(n_big)))
print(f"sum(map(int,..)): {time.perf_counter() - start:.3f} сек")
