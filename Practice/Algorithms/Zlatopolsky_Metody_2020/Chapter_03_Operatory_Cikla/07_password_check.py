# Задача:
# Пользователь вводит пароль. Пока введён неправильный — программа просит снова.
# Максимум 3 попытки. После — блокировка.

CORRECT_PASSWORD = "qwerty"
attempt = 0
MAX_ATTEMPTS = 3

while attempt < MAX_ATTEMPTS:
    password = input("Введите пароль: ")
    if password.lower() == CORRECT_PASSWORD:
        print("Доступ разрешён!")
        break
    else:
        attempt += 1
        remaining = MAX_ATTEMPTS - attempt
        if remaining > 0:
            print(f"Неверный пароль. Осталось попыток: {remaining}")
else:
    # Этот блок сработает, если break НЕ выполнился
    print("Доступ заблокирован!")
