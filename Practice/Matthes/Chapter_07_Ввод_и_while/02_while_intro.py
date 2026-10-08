current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "Введите слово (или 'хватит' для выхода): "
message = ""                                # ← инициализация пустой строкой

while message != 'Хватит':                  # ← условие
    message = input(prompt).title().strip() # ← обновление через input и приводим к единому виду
    if message != 'Хватит':                 # ← Проверка. В случае если пользователь ввёл "хватит", то сообщение не выводится
        print(message)
