# Идея: проверить функцию pluralize через автоматический тест, а не через print.

from pluralize_module import pluralize

# Тестовые случаи: (вход, ожидаемый_результат)
test_cases = [
    (1, "1 акция"),
    (2, "2 акции"),
    (5, "5 акций"),
    (11, "11 акций"),
    (21, "21 акция"),
    (22, "22 акции"),
    (25, "25 акций"),
    (111, "111 акций"),
]

for count, expected in test_cases:
    result = pluralize(count, "акция", "акции", "акций")
    status = "✅" if result == expected else "❌"
    print(f"{status} pluralize({count}) = {result!r} (ожидалось {expected!r})")
