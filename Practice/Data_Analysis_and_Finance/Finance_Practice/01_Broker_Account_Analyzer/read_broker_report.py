import csv
import pprint as p 

def read_broker_report(filepath):
    trades = []
    with open(filepath, mode='r', encoding='utf-8-sig') as file:
        
        # Пропускаем строку заголовков, сохранив её в переменную:
        header_reader = csv.reader(file)
        header = next(header_reader)
        
        # Пропускаем вторую строку, где нет данных:
        file.readline()
        reader = csv.DictReader(file, fieldnames=header)
        
        # Читаем все остальные строки в цикле for:
        for line in reader:
        
            # Защита от пустых строк:
            if not line or not line[header[0]]:
                continue

            trade = (
                    line['Дата заключения'],
                    line['Наименование ЦБ'],
                    line['Код ЦБ'],
                    line['Вид'],
                    int(line['Количество, шт.'].strip().replace(" ", "")),
                    float(line['Цена'].strip().replace(" ", "")),
                    float(line['Сумма'].strip().replace(" ", "")),
                    float(line['НКД'].strip().replace(" ", "")),
                    float(line['Комиссия Брокера'].strip().replace(" ", "")),
                    float(line['Комиссия Биржи'].strip().replace(" ", ""))
                    )
        
            trades.append(trade)
        
    return trades

# print(f"Всего сделок: {len(read_broker_report('data/Сделки.csv'))}\n")
# print(read_broker_report('data/Сделки.csv')[0])
# p.pprint(read_broker_report('data/Сделки.csv'), width=120)



