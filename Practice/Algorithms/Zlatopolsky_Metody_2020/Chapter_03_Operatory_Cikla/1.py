import time

def count_primes(limit):
    count = 0
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count

print("Запуск теста простых чисел (Чистый Python)...")
start = time.perf_counter()
primes_found = count_primes(50_000)
duration = time.perf_counter() - start

print(f"Найдено {primes_found} простых чисел.")
print(f"Время выполнения: {duration:.3f} секунд.")

