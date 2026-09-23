# Задание:
# Возьми ту же строку "AAPL 150.2 100; GOOGL 2800.5 20; TSLA 700.0 50".
#    1. Создай список portfolio через простой цикл for (как я показал выше).
#    2. Создай новый пустой список expensive_stocks.
#    3. Напиши цикл for, который проходит по portfolio и добавляет в expensive_stocks
#       только те словари, у которых price (цена) больше 500.
#    4. Выведи на экран список expensive_stocks и скажи, сколько таких акций нашлось (используй len()).
# Подсказка: Твой код должен содержать два цикла: первый — для разбора строки (уже сделали),
# второй — для фильтрации. Или можно всё сделать в одном цикле сразу при разборе.

import pprint
# Исходные данные:
transaction_data = ["AAPL 175.3 150",
    "GOOGL 2850.0 10",
    "TSLA 710.2 30"]

# Разбиваем строку на отдельные сделки по точке с запятой
deals_raw = transaction_data.split(",")

# Создаём пустой список, куда будем складывать словари
portfolio = []  # Список для словарей всех сделок
expensive_stocks = []  # Список для словарей сделок только с дорогими акциями
# Походим по каждой сделке циклом
for deal in deals_raw:
    parts = (
        deal.strip().split()
    )  # Убираем лишние пробелы по краям и разбиваем по пробелам
    # Извлекаем данные с помощью индексов:
    ticker = parts[0]
    price = float(parts[1])
    quantity = int(parts[2])
    # Создаём словарь для одной сделки:
    deal_dict = {"ticker": ticker, "price": price, "quantity": quantity}
    # Добавляем новую сделку в общий портфель:
    portfolio.append(deal_dict)
    # Отсортировываем сделки с дорогими акциями и добавляем их в свой портфель
    if deal_dict["price"] > 500:
        expensive_stocks.append(deal_dict)


print("===Все сделки===")
pprint.pprint(expensive_stocks)
print("\nДорогие акции (цена более 500)")
pprint.pprint(expensive_stocks)
print(f"Акций с ценой выше 500 всего {len(expensive_stocks)}")
