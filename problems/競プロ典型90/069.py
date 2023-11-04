def mod_pow(x, n, mod):
    if n == 0:
        return 1
    res = mod_pow(x**2 % mod, n//2, mod)
    if n & 1:
        res = res * x % mod
    return res

N, K = map(int,input().split())
MOD = 10**9 + 7

if N == 1:
    print(K % MOD)
elif N == 2:
    print(K * (K - 1) % MOD)
else:
    ans = K * (K - 1)
    ans %= MOD
    cnt = N - 2
    ans2 = mod_pow(K - 2, cnt, MOD)
    ans3 = (ans * ans2) % MOD
    print(ans3)