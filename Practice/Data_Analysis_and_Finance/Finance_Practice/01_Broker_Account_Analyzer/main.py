# Упражнение 1: Простое чтение (без CSV-модуля)
# Цель: Понять, как работает open() и for line in file.
#
# Задача: Напишите программу, которая открывает файл data/trades.csv и выводит каждую строку на экран как есть (в виде строки).

with open('data/trades.csv', mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        
        # 1. Пропускаем пустые строки или строки-комментарии, которые начинаются с #
        if not line or line.startswith('#'):
            continue
            
        # 2. Пропускаем строку заголовков, если встретили её
        if line.startswith('ticker,operation'):
            continue
            
        # Сюда дойдут только строки с реальными данными сделок
        parts = line.split(',')
        trade = (parts[0], parts[1], int(parts[2]), float(parts[3]))
        print(trade)

import csv

with open('data/trades.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)







