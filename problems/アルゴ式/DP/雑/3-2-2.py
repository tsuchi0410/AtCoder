N, M = (int(x) for x in input().split())
W = list(map(int,input().split()))

dp = []
for i in range(N+1):
    dp.append([False]*(M+1))

# 初期値
dp[0][0] = True

for i in range(N):
    for j in range(M+1):
        if not dp[i][j]:
            continue
        
        dp[i+1][j] = True

        if j+W[i] <= M:
            dp[i+1][j+W[i]] = True

print("Yes" if dp[-1][-1] else "No")