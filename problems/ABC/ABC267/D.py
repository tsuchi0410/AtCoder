N, M = (int(x) for x in input().split())
A = list(map(int,input().split()))

INF = float('inf') * -1
dp = []
for i in range(M+1):
    dp.append([INF] * (N+1))


for i in range(M+1):
    for j in range(N+1):
        
        # 初期値
        if i == 0:
            dp[i][j] = 0
        
        if dp[i][j] == INF:
            continue
        
        if i+1 < M+1 and j+1 < N+1:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j] + A[j] * (i+1))

print(dp)        
print(max(dp[-1]))
        