# === ЗАМЕР ПРОИЗВОДИТЕЛЬНОСТИ ===
# (оформляем код без функций, через while-цикл повторений)
import time

# Три алгоритма в виде небольших блоков для замера:

# --- Версия 1: перебор ---
start = time.time()
for _ in range(10000):
    a_test, b_test = 1071, 462
    nod = b_test if b_test < a_test else a_test
    while not (a_test % nod == 0 and b_test % nod == 0):
        nod -= 1
print(f"Версия 1 (перебор):       {time.time() - start:.4f} сек")

# --- Версия 2: Евклид через вычитание ---
start = time.time()
for _ in range(10000):
    a_test, b_test = 1071, 462
    while a_test != b_test:
        if a_test > b_test:
            a_test -= b_test
        else:
            b_test -= a_test
print(f"Версия 2 (вычитание):     {time.time() - start:.4f} сек")

# --- Версия 3: Евклид через остаток ---
start = time.time()
for _ in range(10000):
    a_test, b_test = 1071, 462
    while b_test != 0:
        a_test, b_test = b_test, a_test % b_test
print(f"Версия 3 (остаток):       {time.time() - start:.4f} сек")
