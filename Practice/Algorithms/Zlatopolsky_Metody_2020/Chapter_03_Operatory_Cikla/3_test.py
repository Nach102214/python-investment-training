import multiprocessing
import time
import math

def heavy_computation(duration_seconds=3):
    """Функция, которая загружает одно ядро на 100% заданное время"""
    end_time = time.perf_counter() + duration_seconds
    ops = 0
    while time.perf_counter() < end_time:
        # Тяжелая математика для процессора
        math.sin(ops)
        math.factorial(ops % 500)
        ops += 1
    return ops

if __name__ == "__main__":
    # 1. Определяем количество логических ядер
    cpu_count = multiprocessing.cpu_count()
    print(f"Система обнаружила: {cpu_count} логических ядер (потоков).")
    print(f"Запуск стресс-теста на ВСЕХ ядрах одновременно на 3 секунды...\n")
    
    # 2. Запускаем параллельные процессы
    start_time = time.perf_counter()
    
    with multiprocessing.Pool(processes=cpu_count) as pool:
        # Запускаем задачу для каждого ядра
        results = pool.map(heavy_computation, [3] * cpu_count)
        
    total_time = time.perf_counter() - start_time
    total_operations = sum(results)
    
    print("Тест завершен!")
    print(f"Реальное время выполнения: {total_time:.3f} сек.")
    print(f"Всего выполнено тяжелых математических операций: {total_operations:,}")
    print(f"Индекс многопоточной мощности: {int(total_operations / total_time):_} оп/сек")

