def display_message():
    """Выводит простое сообщение о теме этой главы"""
    print("Изучаем главу №8 'Функции'.")


display_message()


def favorite_book(title):
    """Выводит сообщение с переданным аргументом"""
    print(f'\nОдна из моих любимых книг - "{title}".')


favorite_book("Алиса в стране чудес")


def describe_city(city, country="Russia"):
    """выводит простое сообщение (например, «Рейкьявик находится в Исландии»)"""
    print(f"\nГород {city.title()} находится в стране {country}.")


describe_city("Moskow")
describe_city("irkutsk")
describe_city("berlin", country="Deutschland")


def get_formatted_name(first_name, last_name):
    """Возвращает отформатированное полное имя."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(f"\n{musician}")
