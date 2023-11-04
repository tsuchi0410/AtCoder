L, R = (int(x) for x in input().split())
MOD = 10 ** 9 + 7

digit_L = len(str(L))
digit_R = len(str(R))

ans = 0
for i in range(digit_L - 1, digit_R):
    # 初項
    a = max(10 ** i, L)
    # 末項
    l = min(10 ** (i + 1) - 1, R)
    # 項数
    n = (l - a + 1)
    
    temp = (n * (a + l) // 2) % MOD
    ans += (i + 1) * temp % MOD
    ans %= MOD

print(ans)