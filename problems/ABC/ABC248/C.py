N,M,K = (int(x) for x in input().split())

dp = []
for i in range(N):
    dp.append([0] * (K + 1))

# 初期値
for i in range(1, K + 1):
    if i <= M:
        dp[0][i] = 1

for i in range(N):
    for j in range(K + 1):
        
        if dp[i][j] == 0:
            continue
        if i == N - 1:
            continue
        
        # next
        for k in range(1, M + 1):
            if j + k < K + 1:
                dp[i+1][j+k] += dp[i][j]
        
print(sum(dp[-1]) % 998244353)
