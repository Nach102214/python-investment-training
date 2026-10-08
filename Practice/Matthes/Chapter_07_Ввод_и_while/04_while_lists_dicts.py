# Пример 1 — Перемещение между списками
#
# Как в книге:

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Проверяем пользователя: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nПроверенные пользователи:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Обрати внимание: порядок обратный — потому что .pop() забирает последний элемент. Если нужен прямой порядок — используй .pop(0) (забирает первый).


# Пример 2 — Удаление всех вхождений

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(f"\n{pets}")

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Почему не for? Потому что .remove() сдвигает индексы, и for пропустит элементы. while решает эту проблему: он каждый раз заново проверяет наличие 'cat'.


# Пример 3 — Опрос с сохранением в словарь
#
# Это главный пример. Программа спрашивает имя и гору, сохраняет в словарь, спрашивает — продолжать ли:

responses = {}                  # пустой словарь

polling_active = True           # флаг

while polling_active:
    name = input("\nКак вас зовут? ")
    response = input("На какую гору вы хотели бы подняться? ")

    responses[name] = response  # сохраняем пару

    repeat = input("Продолжить опрос? (да/нет) ")
    if repeat == 'нет':
        polling_active = False

print("\n--- Результаты опроса ---")
for name, response in responses.items():
    print(f"{name} хотел бы подняться на {response}.")



















