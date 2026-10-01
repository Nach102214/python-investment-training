# Закрепление оператора * (распаковка)

# 1. Простой список
nums = [1, 2, 3, 4, 5]

print("Без *:", nums)
print("С *:", *nums)
print("С * и sep:", *nums, sep=", ")
print("С * и sep=' -> ':", *nums, sep=" -> ")

# 2. Список строк
names = ["Аня", "Борис", "Вика"]

print("\nИмена:", *names)
print("Имена с sep:", *names, sep=", ")

# 3. Список списков (вложенный)
matrix = [[1, 2], [3, 4], [5, 6]]

print("\nМатрица:")
print(*matrix, sep="\n")

# 4. Объединение списков через *
a = [1, 2, 3]
b = [4, 5, 6]
combined = [*a, *b]
print(f"\nОбъединение: {combined}")

# 5. Передача списка как аргументов функции
def my_sum(a, b, c):
    return a + b + c

values = [10, 20, 30]
result = my_sum(*values)
print(f"\nmy_sum(*values) = {result}")
