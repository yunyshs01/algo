from math import factorial
n, k = input().split()
n = int(n); k = int(k)
print(factorial(n)//(factorial(n-k) * factorial(k)))