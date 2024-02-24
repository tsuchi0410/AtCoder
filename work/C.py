### Python で提出 ###
from functools import lru_cache
import sys
sys.setrecursionlimit(10**9)

x = int(input())
@lru_cache(maxsize=None)
def f(x):
    
    if x <= 1:
        return 0

    x1 = x // 2
    x2 = (x + 1) // 2
    
    return f(x1) + f(x2) + x

x = f(x)
print(x)