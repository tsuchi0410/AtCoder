N, M = map(int, input().split())
MOD = 998244353
ans = M
for i in range(N - 2):
    ans *= M - 1
    ans %= MOD

print(ans)