# Pythonで提出！！！
from functools import lru_cache

n = int(input())

@lru_cache
def f(x):

    if x <= 0:
        xx = 1
        return xx
    x1 = x // 2
    x2 = x // 3
    
    return f(x1) + f(x2)

x = f(n)
print(x)