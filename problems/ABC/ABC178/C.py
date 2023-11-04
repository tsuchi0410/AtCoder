N = int(input())
MOD = 10 ** 9 + 7

def mod_pow(x, n, mod):
    if n == 0:
        return 1
    res = mod_pow(x**2 % mod, n//2, mod)
    if n & 1:
        res = res * x % mod
    return res

U = mod_pow(10, N, MOD)
A = mod_pow(9, N, MOD)
B = mod_pow(9, N, MOD)
AB = mod_pow(8, N, MOD)

ans = U - (A + B - AB)
print(ans % MOD)