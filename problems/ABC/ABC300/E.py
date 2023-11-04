from functools import lru_cache
import sys
sys.setrecursionlimit(10**9)

@lru_cache(maxsize=None)
def f(x):
    if x == 1:
        return 1
    ans = 0
    for i in range(2, 7):
        if x % i == 0:
            ans += f(x // i)
    ans *= play
    ans %= MOD
    return ans
    
N = int(input())
MOD = 998244353
inv = pow(5, MOD - 2, MOD)
play = (1 * inv) % MOD
ans = f(N)
print(ans)

