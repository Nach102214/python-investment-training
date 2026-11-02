# Task 1: Write a function that displays all unique tickers from the list of trades. Use set.
import read_broker_report as rbr 

def unique_tickers(filepath):
    '''выводит все уникальные тикеры из списка сделок.'''
    data = rbr.read_broker_report(filepath)
    tickers_set = {trade[2] for trade in data}
    return sorted(list(tickers_set))
print(f"Список уникальных тикерров: {unique_tickers('data/Сделки.csv')}")

