import csv
import pprint as p 

def read_broker_report(filepath):
    trades = []
    with open(filepath, mode='r', encoding='utf-8-sig') as file:
        
        # Создаем DictReader. Он САМ возьмет первую строку как заголовок.
        reader = csv.DictReader(file)
        
        # Получаем список настоящих имен колонок (из первой строки файла)
        # Это нужно для проверки на пустоту
        fieldnames = reader.fieldnames
        
        if not fieldnames:
            return trades

        for line in reader:
            
            # 1. Самая надежная защита: проверяем самую первую колонку (Дата заключения)
            # Если она пустая или там текст "Площадка" — пропускаем строку
            first_col_value = line.get(fieldnames[0], "").strip()
            
            # Пропускаем пустые строки и строки-разделители (где нет даты)
            if not first_col_value or "Площадка" in first_col_value or "Всего" in first_col_value:
                continue

            # 2. Защита от нечисловых значений
            try:
                qty = int(line['Количество, шт.'].strip().replace(" ", ""))
                price = float(line['Цена'].strip().replace(" ", ""))
                amount = float(line['Сумма'].strip().replace(" ", ""))
                aci = float(line['НКД'].strip().replace(" ", ""))
                broker_fee = float(line['Комиссия Брокера'].strip().replace(" ", ""))
                exchange_fee = float(line['Комиссия Биржи'].strip().replace(" ", ""))
            except (ValueError, TypeError, KeyError):
                # Если в строке ошибка или колонка называется иначе — пропускаем
                continue

            trade = (
                line['Дата заключения'],
                line['Наименование ЦБ'],
                line['Код ЦБ'],
                line['Вид'],
                qty, price, amount, aci, broker_fee, exchange_fee
            )
            trades.append(trade)
        
    return trades

if __name__=='__main__':
    data = read_broker_report('data/Сделки.csv')
    
    print(f"Всего сделок: {len(data)}\n")
    
    if data:
        print("Первая сделка:")
        print(data[0])
        
        print("\nВсе сделки (pprint):")
        p.pprint(data[:5], width=120) # Выведем первые 5 для проверки
    else:
        print("Данные не загружены. Проверьте имена колонок в файле.")
        # Для диагностики: выведем первые 2 строки файла как есть
        with open('data/Сделки.csv', encoding='utf-8-sig') as f:
            for i, line in enumerate(f):
                if i < 3:
                    print(f"Строка {i+1}: {repr(line)}")



