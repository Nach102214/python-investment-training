def get_total_amount_by_type(filepath):
    '''Находит общую сумму всех сделок'''
    import read_broker_report as rbr

    amounts = {}

    for trade in rbr.read_broker_report(filepath):
        ticker = trade[1]
        action = trade[3]
        amount = trade[6]

        # Создаем базовую структуру для нового тикера
        if ticker not in amounts:
            amounts[ticker] = {'Покупка': 0.0, 'Продажа': 0.0} 

        # Проверяем, что вид сделки корректный, и прибавляем сумму к нужному ключу
        if action in amounts[ticker]:
            amounts[ticker][action] += amount
        
        # Округляем результат до двух знаков после запятой
    for ticker in amounts:
            amounts[ticker]['Покупка'] = round(amounts[ticker]['Покупка'], 2)
            amounts[ticker]['Продажа'] = round(amounts[ticker]['Продажа'], 2)

    return amounts


if __name__=='__main__':
    import pprint as p
    p.pprint(get_total_amount_by_type('data/Сделки.csv'), width=90)
