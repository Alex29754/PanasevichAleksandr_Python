from math import factorial

n = int(input())

for j in range(n):
    print(' ' * (n - j), end='')
    l = [int(factorial(j)/(factorial(i) * factorial(j - i))) for i in range(j + 1)]
    print(*l)
