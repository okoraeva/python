import math


def transpose(n):
    return math.factorial(n)


def arange(n, k):
    return (math.factorial(n))/(math.factorial(n-k))


def combine(n, k):
    return (math.factorial(n))/(math.factorial(k)*(math.factorial(n-k)))


print(combine(12, 2))

