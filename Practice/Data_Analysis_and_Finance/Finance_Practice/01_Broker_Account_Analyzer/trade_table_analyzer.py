# Набор функций для анализа таблицы сделок из отчёта брокера СБ

import csv
import pprint

def read_broker_report(filepath):
    '''Читает отчёт брокера и сохраняет его в список сделок'''
    # Создаём переменную с пустым списком
    trades = []

    # Открываем файл по пути filepath, только для чтения, с кодировкой
    with open(filepath, mode='r', encoding='utf-8-sig') as file:

        # Создаём DictReader. Он сам определить строку как заголовок:
        reader = csv.DictReader(file)

        # Получаем список настоящих имён колонок:
        fieldnames = reader.fieldnames

        # Проверяем строку заголовков на пустоту:
        if not fieldnames:
            return trades

        # проходим циклом по всем строкам:
        for line in reader:

            # Проверяем самый первый столбец (Дата заключения)
            # Если он пустой или там текст "Площадка", то пропускаем строку:
            first_col_value = line.get(fieldnames[0], "").strip().capitalize()

            if not first_col_value or "Площадка" in first_col_value or "Всего" in first_col_value:
                continue

            # Проверяем последний столбец (Статус сделки)
            # Если он не равен "ЗИ" или "И", то пропускаем строку:
            last_col_value = line.get(fieldnames[-1], "").strip().upper()

            if last_col_value not in ["ЗИ", "И"]:
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

    print(f"Всего сделок - {len(data)}")
    print("\nВсе сделки: ")
    pprint.pprint(data, width=120)
