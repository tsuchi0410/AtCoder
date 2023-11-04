N = int(input())
MOD = 998244353
L = []
for i in range(N):
    A, B = map(int, input().split())
    L.append([A, B])

dp = [[0, 0] for _ in range(N)]
dp[0][0] = 1
dp[0][1] = 1
for i in range(1, N):
    
    num = 0
    # 表
    if L[i][0] != L[i - 1][0]:
        num += dp[i - 1][0]
    if L[i][0] != L[i - 1][1]:
        num += dp[i - 1][1]
    dp[i][0] = num % MOD

    num = 0
    # 裏
    if L[i][1] != L[i - 1][0]:
        num += dp[i - 1][0]
    if L[i][1] != L[i - 1][1]:
        num += dp[i - 1][1]
    dp[i][1] = num % MOD

ans = (dp[N - 1][0] + dp[N - 1][1]) % MOD
print(ans)

