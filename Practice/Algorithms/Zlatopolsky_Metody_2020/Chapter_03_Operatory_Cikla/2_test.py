import time
import numpy as np

# Создаем две случайные матрицы 2000x2000
size = 2000
matrix_a = np.random.rand(size, size)
matrix_b = np.random.rand(size, size)

print("Запуск матричного умножения (NumPy)...")
start = time.perf_counter()

# Перемножение матриц
matrix_c = np.dot(matrix_a, matrix_b)

duration = time.perf_counter() - start
print(f"Матрицы {size}x{size} успешно перемножены.")
print(f"Время выполнения: {duration:.3f} секунд.")

