# Задача написать функцию, которая возвращает правильную форму слова для числа count.

## Условие

    Правила: 1, 21, 31... → «акция»; 2-4, 22-24... → «акции»; 5-20, 25-30... → «акций»

#### Логика:

    1, 21, 31... (оканчивается на 1, кроме 11) → word1.
    2-4, 22-24... (оканчивается на 2, 3, 4, кроме 12-14) → word2.
    Остальные → word5.

```python
def pluralize(count, word1, word2, word5):
    """Возвращает правильную форму слова для числа count."""
    last_digit = count % 10
    last_two = count % 100

    if last_digit == 1 and last_two != 11:
        form = word1
    elif last_digit in (2, 3, 4) and last_two not in (12, 13, 14):
        form = word2
    else:
        form = word5

    return f"{count} {form}"


result = pluralize(10, 'акция', 'акции', 'акций')
print(result)

# Тест:
test_counts = range(0, 23)
for num in test_counts:
    res = pluralize(num, "акция", "акции", "акций")
    print(res)
```
