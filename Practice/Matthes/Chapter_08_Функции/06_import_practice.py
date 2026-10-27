# Вариант 1: модуль целиком + вызов через имя модуля
import pluralize_module
print(pluralize_module.pluralize(3, "акция", "акции", "акций"))

# Вариант 2: конкретная функция
from pluralize_module import pluralize
print(pluralize(5, "акция", "акции", "акций"))

# Вариант 3: псевдоним функции
from pluralize_module import pluralize as pl
print(pl(22, "акция", "акции", "акций"))
