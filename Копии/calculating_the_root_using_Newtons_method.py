# Ищем корень квадратный из числа методом Ньютона
x = 14
epsilon = 0.00000000000001
guess = x / 2
while abs(guess*guess - x) > epsilon:
    guess = (guess + x/guess) / 2

print(guess)
