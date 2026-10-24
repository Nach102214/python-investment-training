# Задача 1. Футболка (упражнение 8.3)
# Напишите функцию make_shirt(), которая получает размер
# футболки и текст, который должен быть напечатан на ней. Функция должна вы-
# водить сообщение с размером и текстом.
# Вызовите функцию с помощью позиционных аргументов. Вызовите функцию во
# второй раз с помощью именованных аргументов.


def make_shirt(size, message):
    print(f"Размер {size}, текст: {message}")

make_shirt("L", "I love Python")

make_shirt(size="XL", message="My name is Sergey")

# Задача 2. Большие футболки (упражнение 8.4)
#  Измените функцию make_shirt(), чтобы футболки по
# умолчанию имели размер L и на них выводился текст «Я люблю Python». Создайте
# футболку с размером L и текстом по умолчанию, а также футболку любого раз-
# мера с другим текстом.


def make_shirt(size="L", message="I love Python"):
    print(f"Размер {size}, текст: {message}")

make_shirt()
make_shirt("M")

make_shirt(size="XL", message="My name is Sergey")


# 8.5. Города. Напишите функцию describe_city(), которая получает названия
# города и страны. Функция должна выводить простое сообщение (например, «Рей-
# кьявик находится в Исландии»). Задайте параметру страны значение по умолча-
# нию. Вызовите свою функцию для трех разных городов, по крайней мере один из
# которых не находится в стране по умолчанию.

def describe_city(city, country="Russia"):
    full_string = f"{city}, {country}"
    return full_string.title()

print(describe_city("Moscow"))
print(describe_city("Irkutsk"))
print(describe_city("Tambov"))


# Задача 4. Профиль пользователя (упражнение 8.13)
# Создайте собственный профиль с помощью вызова build_profile(),
# укажите имя, фамилию и три другие пары «ключ — значение» для вашего описания.

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Алексей', 'Иванов', age=30, city='Москва', job='инженер')
print(user_profile)











