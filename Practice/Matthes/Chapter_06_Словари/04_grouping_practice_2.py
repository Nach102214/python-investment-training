# ============================================================
# Задача 1: Группировка транзакций по типу
# ============================================================
# Дано: список транзакций. У каждой есть type («покупка» или «продажа») и amount (сумма).
transactions = [
    {"type": "покупка", "amount": 10000},
    {"type": "продажа", "amount": 5000},
    {"type": "покупка", "amount": 25000},
    {"type": "продажа", "amount": 3000},
    {"type": "покупка", "amount": 7000},
]

# Нужно: сгруппировать сумму транзакций по типу.
# Ожидаемый результат:
# покупка: 42000
# продажа: 8000

by_type = {}
for t in transactions:
    t_type = t["type"]
    amount = t["amount"]
    if t_type in by_type:
        by_type[t_type] += amount      # ✅ число: +=
    else:
        by_type[t_type] = amount

print("Задача 1:")
for t_type, total in by_type.items():
    print(f"{t_type}: {total}")


# ============================================================
# Задача 2: Группировка студентов по оценкам
# ============================================================
students = [
    {"name": "Анна", "grade": 5},
    {"name": "Борис", "grade": 3},
    {"name": "Вера", "grade": 5},
    {"name": "Глеб", "grade": 4},
    {"name": "Дина", "grade": 5},
    {"name": "Егор", "grade": 3},
]
# Нужно: сгруппировать имена студентов по оценкам. Для каждой оценки — список имён.

by_grade = {}
for student in students:
    grade = student["grade"]
    name = student["name"]
    if grade in by_grade:
        by_grade[grade].append(name)   # ✅ список: .append()
    else:
        by_grade[grade] = [name]

print("\nЗадача 2:")
for grade, names in sorted(by_grade.items(), reverse=True):
    print(f"{grade}: {names}")


# ============================================================
# Задача 3: Подсчёт частоты слов
# ============================================================
words = ["python", "код", "python", "файл", "код", "python", "список", "файл"]
# Нужно: посчитать, сколько раз встречается каждое слово.

counts = {}
for word in words:
    if word in counts:
        counts[word] += 1              # ✅ счётчик: += 1
    else:
        counts[word] = 1

print("\nЗадача 3:")
for word, count in counts.items():
    print(f"{word}: {count}")
