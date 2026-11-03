# Задача 2: Подсчитать количество сделок по каждому тикеру (словарь)

def number_of_trades_for_each_ticker(filepath):
    '''Подсчитывает количество сделок по каждому тикеру'''
    import read_broker_report as rbr 

    counts = {}
    
    for trade in rbr.read_broker_report(filepath):
        ticker = trade[1]
        view = trade[3]
        if ticker not in counts:
            counts[ticker] = {'Покупка': 0, 'Продажа': 0}

        if view in counts[ticker]:
            counts[ticker][view] += 1

    return counts

if __name__=='__main__':

    import pprint as p
    print("Сделки по тикерам и видам:")
    p.pprint(number_of_trades_for_each_ticker('data/Сделки.csv'))

