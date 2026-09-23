# data = "2024-07-23,AAPL,185.50,186.20,184.80,185.90,10000000"
#
# # Разбиваем по запятой
# parts = data.split(',')
# date_str_ru = '.'.join(parts[0].split('-')[::-1])
# ticker = parts[1]
# open_p = float(parts[2])
# high_p = float(parts[3])
# low_p = float(parts[4])
# close_p = float(parts[5])
# volume = int(parts[6])
#
# # Вычисляем дневной диапазон и изменение
# day_range = high_p - low_p
# change = close_p - open_p
#
# # Формируем отчёт
# report = (
#     f"Дата: {date_str_ru}\n"
#     f"Тикер: {ticker}\n"
#     f"Открытие: {open_p:.2f}, Закрытие: {close_p:.2f}\n"
#     f"Диапазон: {day_range:.2f} ({high_p:.2f} - {low_p:.2f})\n"
#     f"Изменение: {change:+.2f}\n"
#     f"Объём: {volume:,}"
# )
# print(report)
"============================================================================"
print("=== Задача 1 (очистка тикеров) ===")
# У тебя есть список «грязных» тикеров:
# [" AAPL", "msft ", " GoogL ", " amzn "]
# Приведи их к единому формату: удали пробелы и переведи в верхний регистр. 
# Проверь, содержит ли какой-то тикер подстроку "GO" (должен найти GOOGL).

ticker_raw = [" AAPL", "msft ", " GoogL ", " amzn "]
ticker_clean = ','.join(ticker_raw).strip().replace(' ', '').upper()
start_index = ticker_clean.find('GO')
end_index = ticker_clean.find(',', start_index)
find_ticker = ticker_clean[start_index:end_index]

print(f"\nОчищенные тикеры: {ticker_clean}")
print(f"\nВ них имеется строка, содержащая 'GO', это '{find_ticker}'")

"============================================================================"
print("\n=== Задача 2 (парсинг валютной пары) ===")
# Дана строка "EUR/USD=1.0850". Вытащи базовую валюту, валюту котировки и курс как число. 
# Выведи: Базовая валюта: EUR, котируемая: USD, курс 1.0850.

str_raw = "EUR/USD=1.0850"
base_currency = str_raw[:str_raw.find('/')]
quote_currency = str_raw[str_raw.find('/')+1:str_raw.find('=')]
exchange_rate = str_raw[str_raw.find('=')+1:]

print(f"\nБазовая валюта: {base_currency}, котируемая: {quote_currency}, курс {exchange_rate}")

"============================================================================"
print("\n=== Задача 3 (анализ заголовка новости) ===")
# Заголовок: "Акции Apple выросли на 5% после отчёта о прибыли". 
# Подсчитай, сколько раз встречается слово «прибыл» (как часть слова) с помощью метода .count(). 
# Проверь, начинается ли заголовок с «Акции» (.startswith()). 
# Выведи первое слово заголовка через срез до первого пробела.

title = "Акции Apple выросли на 5% после отчёта о прибыли"
count_examination = title.lower().count('прибыл')
start_examination = title.upper().startswith('АКЦИИ')

print(f"\nЗаголовок начинается со слова '{title[:title.find(' ')]}'")










