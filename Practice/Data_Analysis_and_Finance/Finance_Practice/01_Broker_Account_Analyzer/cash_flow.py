import csv
import pprint as p 

def cash_flow(filepath):
    '''Функция выделяет суммы зачислений, выводы средств и комиссии на счёте'''
    cash = {
        'Введено средств': 0.0,
        'Выведено средств': 0.0,
        'Уплачено комиссий': 0.0,
    }

    with open(filepath, mode='r', encoding='utf-8-sig') as file:
        # Стандартный разделитель — запятая
        reader = csv.reader(file)
        
        # Пропускаем строку заголовков
        next(reader, None) 

        for line in reader:
            # Защита от пустых строк
            if not line or len(line) < 6:
                continue

            # Очищаем описание операции для проверки условий
            operation = line[2].strip().lower()

            # Функция для безопасного перевода строки с пробелами/запятыми в float
            def to_float(val):
                cleaned = val.strip().replace(" ", "").replace("\xa0", "").replace(",", ".")
                return float(cleaned) if cleaned else 0.0

            # 1. КОМИССИИ И ДЕПОЗИТАРНЫЕ УСЛУГИ
            # Проверяем, начинается ли строка с "комиссия" или содержит оплату услуг
            if operation.startswith('комиссия') or 'оплата депозитарных' in operation:
                # Сумма списания за комиссию находится в последней колонке (индекс 5)
                cash['Уплачено комиссий'] += to_float(line[5])

            # 2. ВВЕДЕНО СРЕДСТВ
            elif operation == 'зачисление д/с':
                cash['Введено средств'] += to_float(line[4])

            # 3. ВЫВЕДЕНО СРЕДСТВ
            elif operation == 'списание д/с':
                cash['Выведено средств'] += to_float(line[5])

    # Округляем результаты для исключения погрешностей float
    for key in cash:
        cash[key] = round(cash[key], 2)

    return cash

if __name__ == '__main__':
    # Пример запуска
    result = cash_flow('ДДС.csv')
    p.pprint(result, width=120)

    difference = result['Введено средств'] - result['Выведено средств']
    print(f"\nРазница - {difference:.2f}")







