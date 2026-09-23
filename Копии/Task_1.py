ice_cream_prices = [20, 90, 150, 130, 110]
ice_cream_names = ["Ваниль", "Шоколад", "Клубника", "Фисташка", "Карамель"]
max_price = max(ice_cream_prices)
print(f"Самая дорогая цена {max_price}")
total_revenue = sum(ice_cream_prices)
print(f"Общая выручка, если продашь по 1 штуке каждого {total_revenue}")
index_max_price = ice_cream_prices.index(max_price) 
print(f"Самое дорогое мороженое: {ice_cream_names[index_max_price]}")


