# # Цель: перестать бояться типов и переменных в генераторах.
# # Задание 1: Определи тип
# # Напиши в комментарии тип каждого генератора (до запуска!), потом запусти и проверь:
#
data = [10, 20, 30, 40, 50]

a = [x * 2 for x in data]  # тип: int?
print(type(a[0]))
b = [x / 2 for x in data]  # тип: float?
print(type(b[0]))
c = [x for x in data if x > 25]  # тип: int?
print(type(c[0]))
d = [str(x) for x in data]  # тип: str?
print(type(d[0]))
e = [f"число: {x}" for x in data]  # тип: str?
print(type(e[0]))
f = [x % 2 == 0 for x in data]  # тип: bool?
print(type(f[0]))
#
# Задание 2: Обратный перевод (генератор → цикл)
# Даны генераторы. Запиши их в виде обычного цикла. Проверь, что результаты совпадают.

data = [10, 20, 30, 40, 50]

gen_1 = [x + 5 for x in data]
gen_1_cycle = []
for x in data:
    gen_1_cycle.append(x + 5)
print(f"\nСписки совпадают? {gen_1 == gen_1_cycle}")

gen_2 = [x for x in data if x != 30]
gen_2_cycle = []
for x in data:
    if x != 30:
        gen_2_cycle.append(x)
print(f"Списки совпадают? {gen_2 == gen_2_cycle}")

gen_3 = ["большое" if x > 30 else "маленькое" for x in data]
gen_3_cycle = []
for x in data:
    if x > 30:
        gen_3_cycle.append("большое")
    else:
        gen_3_cycle.append("маленькое")
print(f"Списки совпадают? {gen_3 == gen_3_cycle}")

gen_4 = [x * 2 for x in data if x < 40]
gen_4_cycle = []
for x in data:
    if x < 40:
        gen_4_cycle.append(x * 2)
print(f"Списки совпадают? {gen_4 == gen_4_cycle}")

gen_5 = [f"значение: {x}" for x in data]
gen_5_cycle = []
for x in data:
    gen_5_cycle.append(f"значение: {x}")
print(f"Списки совпадают? {gen_5 == gen_5_cycle}")


# Задачи (все через генераторы):
#     Список строк: "Аня: 75 баллов".
#     Список студентов с оценкой ≥ 90.
#     Список групп, в которых учатся отличники (оценка ≥ 90).
#     Список строк: "Аня (A): 75" (имя, группа, балл).
#     Список строк: "Аня: отличник" или "Аня: хорошист" (порог 90).
#     Средний балл (через sum(scores) / len(scores)).

students = ["Аня", "Борис", "Вика", "Гриша", "Даша"]
scores = [75, 92, 88, 65, 95]
groups = ["A", "B", "A", "B", "A"]

list_of_strings_1 = [
    f"{student}: {score} баллов" for student, score in zip(students, scores)
]
print(f"\n{list_of_strings_1}")

list_of_top_students = [
    student for student, score in zip(students, scores) if score >= 90
]
print(f"Список студентов с оценкой больше или равно 90: {list_of_top_students}")

list_of_groups_of_excellent_students = [
    group for student, score, group in zip(students, scores, groups) if score >= 90
]
print(
    f"Список групп, в которых учатся отличники (оценка ≥ 90): {list_of_groups_of_excellent_students}"
)

list_string_2 = [
    f"{student} ({group}): {score}"
    for student, group, score in zip(students, groups, scores)
]
print(list_string_2)

list_string_3 = [
    f"{student}: {'отличник' if score >= 90 else 'хорошист'}"
    for student, score in zip(students, scores)
]
print(list_string_3)

average_score = sum(scores) / len(scores)
print(f"Средний бал равен {average_score}")
