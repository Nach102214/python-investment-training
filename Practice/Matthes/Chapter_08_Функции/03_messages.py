# Упражнение 8.9.
#  Создайте список с серией коротких сообщений. Передайте список
# функции show_messages(), которая выводит текст каждого сообщения в списке.

def show_messages(messages):
    for message in messages:
        print(message)

messages = ["Привет!", "Я приступил к изучению Python!", "Мне не очень легко.", 
            "Но я стараюсь"]
show_messages(messages)

