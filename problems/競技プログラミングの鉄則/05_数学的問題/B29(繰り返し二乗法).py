def mod_pow(x, n, mod):
    if n == 0:
        return 1
    res = mod_pow(x**2 % mod, n//2, mod)
    if n & 1:
        res = res * x % mod
    return res

a, b = map(int,input().split())
MOD = 10**9 + 7
print(mod_pow(a, b, MOD))
