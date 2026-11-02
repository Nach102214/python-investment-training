
print("Упражнение 1: Простое чтение (без CSV-модуля):\n")
#
# Цель: Понять, как работает open() и for line in file.
#
# Задача: Напишите программу, которая открывает файл data/trades.csv и выводит каждую строку на экран как есть (в виде строки).
#
# Ожидаемый результат:
# ticker,operation,quantity,price
# SBER,BUY,10,250.5
# GAZP,BUY,20,180.2
# ...

with open('data/trades.csv', mode='r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())

print("\nУпражнение 2: Чтение и разделение строк:\n")
#
# Цель: Научиться разбивать строку на части с помощью split().
#
# Задача: Прочитайте файл построчно. Для каждой строки (кроме первой, заголовка) разделите её по запятой и выведите на экран список из 4 элементов.
# Ожидаемый результат:
# ['SBER', 'BUY', '10', '250.5']
# ['GAZP', 'BUY', '20', '180.2']
# ...


with open('data/trades.csv', mode='r', encoding='utf-8') as file:
    # Пропускаем первую строку (строку заголовков)
    next(file)
    for line in file:
        parts = line.strip().split(',')
        print(parts)

print("\nУпражнение 3: Чтение с преобразованием типов:\n")
#
# Цель: Научиться преобразовывать строки в числа.
#
# Задача: Модифицируйте упражнение 2 так, чтобы quantity было int, а price — float. Выведите на экран кортеж, как в вашем рабочем коде.

with open('data/trades.csv', mode='r', encoding='utf-8') as file:
    next(file)
    for line in file:
        parts = line.strip().split(',')
        trade = (parts[0], parts[1], int(parts[2]), float(parts[3]))
        print(trade)

print("\nУпражнение 4: Использование csv.DictReader:\n")
#
# Цель: Понять, как работает csv.DictReader и почему он удобен.
#
# Задача: Прочитайте файл с помощью csv.DictReader. Для каждой строки выведите на экран словарь, где ключи — это заголовки столбцов.

import csv

with open('data/trades.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

print("\nУпражнение 5: Сборка всего вместе: \n")
#
# Цель: Собрать все знания в одну функцию.
#
# Задача: Напишите функцию read_trades_from_csv(filepath), которая:
#
#     Открывает файл.
#
#     Использует csv.DictReader.
#
#     Для каждой строки создает кортеж (ticker, operation, quantity, price) с правильными типами.
#
#     Возвращает список этих кортежей.

import pprint as p 
def read_trades_from_csv(filepath):
    trades = []
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            trade = (
                    row['ticker'],
                    row['operation'],
                    int(row['quantity']),
                    float(row['price'])
                    )
            trades.append(trade)

    return trades

trades_data = read_trades_from_csv('data/trades.csv')
p.pprint(trades_data)









