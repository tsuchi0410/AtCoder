n, a, b = map(int, input().split())
MOD = 10**9 + 7

def mod_pow(x, n, mod):
    if n == 0:
        return 1
    res = mod_pow(x**2 % mod, n//2, mod)
    if n & 1:
        res = res * x % mod
    return res

# 二項係数 nCr を高速に計算 O(N + logM)
def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

##################################################
p = 10 ** 9 + 7  # MOD
N = min(n, 2 * 10**5) # N は必要分だけ用意する
##################################################

fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)


# N 種類の花を使って作れる花束の数は 2^n
# 最低一本は選ぶので 2^n - 1
ans = mod_pow(2, n, MOD)
cnt1 = cmb(N, a, MOD)
cnt2 = cmb(N, b, MOD)
print((ans - cnt1 - cnt2) % MOD)