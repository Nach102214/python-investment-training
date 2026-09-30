# Задание: три способа — один результат
# Цель: закрепить знания по использованию тернарного оператора

students = ["Аня", "Борис", "Вика", "Гриша", "Даша", "Егор", "Женя"]
scores = [75, 92, 88, 65, 95, 45, 60]

# Задача: реши тремя способами и убедись, что результаты одинаковы.

# Способ 1: Вложенный тернарный:
result_1 = [
    f"{s}: {'отличник' if sc >= 90 else 'хорошист' if sc >= 80 else 'троечник' if sc >= 60 else 'двоечник'}"
    for s, sc in zip(students, scores)
]
# Способ 2: Обычный цикл с if-elif-else:
result_2 = []
for s, sc in zip(students, scores):
    if sc >= 90:
        status = "отличник"
    elif sc >= 80:
        status = "хорошист"
    elif sc >= 60:
        status = "троечник"
    else:
        status = "двоечник"
    result_2.append(f"{s}: {status}")

# Способ 3: Функция + генератор:
def get_status(score):
    if score >= 90:
        return "отличник"
    elif score >= 80:
        return "хорошист"
    elif score >= 60:
        return "троечник"
    else:
        return "двоечник"

result_3 = [f"{s}: {get_status(sc)}" for s, sc in zip(students, scores)]

print(result_1)
print("\nРезультаты одинаковы? ", result_1 == result_2 == result_3)




















