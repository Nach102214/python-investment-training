# Задача:
# Подберите на своём компьютере такое конечное значение параметра «пустого цикла», 
# при котором будет получаться пауза длительностью примерно в 5 секунд.

import time

# Замеряем время для небольшого базового числа итераций:
test_iterations = 10_000_000
start_time = time.perf_counter()

for _ in range(test_iterations):
    pass

end_time = time.perf_counter()

# Продолжительность теста:

test_duration = end_time - start_time 

# сколько итераций выполняется за 1 секунду
iterations_per_second = test_iterations / test_duration

print(f"{test_iterations} итераций на этом ПК выполняется за {test_duration:.3f} сек.")
print(f"За одну секунду выполняется {int(iterations_per_second):_} итераций")

target_duration = 5
final_iterations = iterations_per_second * target_duration

print(f"За {target_duration} на этом ПК выполнится {int(final_iterations):_}")




