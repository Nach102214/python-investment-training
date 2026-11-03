# Задача 1: Напишите функцию, которая выводит все уникальные тикеры из списка сделок. Используйте множество (set).

def unique_tickers(filepath):
    import csv
    '''выводит все уникальные тикеры из списка сделок.'''
    trades = []
    with open(filepath, mode='r', encoding='utf-8-sig') as f:
        header_reader = csv.reader(f)
        header = next(header_reader)

        f.readline()
        reader = csv.DictReader(f, fieldnames=header)
        for line in reader:

            if not line or not line[header[0]]:
                continue

            trade = (
                    line['Наименование ЦБ']
                    )
            trades.append(trade)

    return sorted(set(trades))

if __name__=='__main__':

    print("Список уникальных тикерров:")
    for ticker in unique_tickers('data/Сделки.csv'):
        print(ticker)

