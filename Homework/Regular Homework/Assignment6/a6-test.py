
from math import sqrt

def fibonacci(n):
    n = 0
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

fibonacci(n)