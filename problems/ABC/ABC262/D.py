MOD = 998244353

N = int(input())
a = list(map(int, input().split()))

dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N)]
#dp[0][0][0] = 1
for i in range(N):
    for j in range(N):
        for k in range(N):
            # 初期値
            if j == 0 and k == 1:
                dp[i][j][k] += 1
            
            if dp[i][j][k] != 0 and i + 1 < N:
                # under
                dp[i + 1][j][k] += dp[i][j][k]
                #next
                amari = (j + a[i + 1]) % (k + 1)
                dp[i + 1][amari][k + 1] += dp[i][j][k]
            
            dp[i][j][k] %= MOD

for i in dp:
    print(i)