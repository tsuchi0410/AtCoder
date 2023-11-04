import pypyjit
pypyjit.set_param('max_unroll_recursion=0')

import sys
sys.setrecursionlimit(10 ** 8)

def mod_pow(x, n, mod):
    if n == 0:
        return 1
    res = mod_pow(x**2 % mod, n//2, mod)
    if n & 1:
        res = res * x % mod
    return res

MOD = 10**9 + 7
a, b = map(int, input().split())
print(mod_pow(a, b, MOD))