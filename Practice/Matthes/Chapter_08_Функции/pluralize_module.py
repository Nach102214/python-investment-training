
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

