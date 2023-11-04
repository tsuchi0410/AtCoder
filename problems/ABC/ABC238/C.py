N = int(input())
MOD = 998244353
ans = 0
while N != 0:
    a = 10 **(int(len(str(N))) - 1)
    d = N - a + 1
    ans += d * (1 + d) // 2
    N = a - 1
    ans %= MOD
print(ans)
