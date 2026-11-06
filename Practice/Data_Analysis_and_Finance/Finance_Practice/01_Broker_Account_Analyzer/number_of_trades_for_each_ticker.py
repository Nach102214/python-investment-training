# Задача 2: Подсчитать количество сделок по каждому тикеру (словарь)

def number_of_trades_for_each_ticker(filepath):
    '''Подсчитывает количество сделок по каждому тикеру'''
    import trade_table_analyzer as rbr 

    counts = {}
    
    for trade in rbr.read_broker_report(filepath):
        ticker = trade[1]
        view = trade[3]
        quantity = trade[4]
        amount = trade[6] + trade[7]
        if ticker not in counts:
            counts[ticker] = {'Покупка': 0, 
                              'Продажа': 0, 
                              'Сумма покупок': 0, 
                              'Сумма продаж': 0
                              }

        if view == "Покупка": 
            counts[ticker]["Покупка"] += quantity
            counts[ticker]["Сумма покупок"] += amount

        if view == "Продажа":
            counts[ticker]["Продажа"] += quantity
            counts[ticker]["Сумма продаж"] += amount
    
    # Округляем суммы до двух знаков после запятой:
    for ticker in counts:
            counts[ticker]["Сумма покупок"] = round(counts[ticker]["Сумма покупок"], 2)
            counts[ticker]["Сумма продаж"] = round(counts[ticker]["Сумма продаж"], 2)
 
    return counts

if __name__=='__main__':

    import pprint as p
    print("Сделки по тикерам и видам:")
    p.pprint(number_of_trades_for_each_ticker('data/Сделки.csv'), width=120)

