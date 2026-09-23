#Задачи:

    # 1. Напиши цикл, который выводит на экран: "День N: Москва - X°, Питер - Y°, 
    #    Казань - Z°" для каждого из 7 дней. (Подсказка: используй range(7) и индексы списков).
    #
    # 2. Найди среднюю температуру за неделю для каждого города (используй цикл 
    #   for для суммирования, а затем подели на длину списка). Не используй sum() 
    #   и len() (искусственно запрещаю! Хочу, чтобы ты прочувствовал, как работают циклы).
    #
    # 3. Найди максимальную температуру за неделю для каждого города (снова цикл, без max()).


# moscow_temps = [20, 22, 19, 21, 23, 18, 20]
# spb_temps = [18, 19, 17, 16, 20, 21, 19]
# kazan_temps = [22, 24, 21, 20, 23, 25, 22]
#
# for i in range(7):
#     t_moscow = moscow_temps[i] 
#     t_spb = spb_temps[i]
#     t_kazan = kazan_temps[i]
#     print(f"День {i + 1}: Москва - {t_moscow}, Питер - {t_spb}, Казань - {t_kazan}")
#
# average_t_moscow = 0
# average_t_spb = 0
# average_t_kazan = 0
#
# for i in moscow_temps:
#     amt = 0
#     amt += 1
#     average_t_moscow =+ i
#
# for i in spb_temps:
#     amt = 0
#     amt += 1
#     average_t_spb =+ i
#
# for i in kazan_temps:
#     amt = 0
#     amt += 1
#     average_t_kazan =+ i
#
# print(f"Средняя температура по городу Москва за неделю {average_t_moscow / amt}")
# print(f"Средняя температура по городу Санкт Петербург за неделю {average_t_spb / amt}")
# print(f"Средняя температура по городу Казань за неделю {average_t_kazan / amt}")
#
#
# max_t_moscow = 0
# max_t_spb = 0
# max_t_kazan = 0
#
# for i in moscow_temps:
#     if i > max_t_moscow:
#         max_t_moscow = i
#
# for i in spb_temps:
#     if i > max_t_spb:
#         max_t_spb = i
#
# for i in kazan_temps:
#     if i > max_t_kazan:
#         max_t_kazan = i
#
# print(f"Максимальная температура по городу Москва за неделю {max_t_moscow}")
# print(f"Максимальная температура по городу Санкт Петербург за неделю {max_t_spb}")    
# print(f"Максимальная температура по городу Казань за неделю {max_t_kazan}")  
#
# Решение DeepSeek:
moscow_temps = [20, 22, 19, 21, 23, 18, 20]
spb_temps = [18, 19, 17, 16, 20, 21, 19]
kazan_temps = [22, 24, 21, 20, 23, 25, 22]

cities = {
    "Москва": moscow_temps,
    "Питер": spb_temps,
    "Казань": kazan_temps
}

# 1. Вывод по дням (используем zip для одновременного прохода по трём спискам)
print("=== Погода по дням ===")
for day, (m, s, k) in enumerate(zip(moscow_temps, spb_temps, kazan_temps), start=1):
    print(f"День {day}: Москва - {m}°, Питер - {s}°, Казань - {k}°")

print("\n=== Статистика ===")
# 2. Средняя и максимальная температура для каждого города
for city, temps in cities.items():
    total = 0
    max_temp = temps[0]
    count = 0
    
    for temp in temps:
        total += temp
        count += 1
        if temp > max_temp:
            max_temp = temp
    
    average = total / count
    print(f"{city}: средняя {average:.1f}°, максимальная {max_temp}°")
