INF = 10**18
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

dp = [[INF] * (2 ** N) for _ in range(M)]
for i in range(M):
    for j in range(2 ** N):
        v = 0
        for k in range(N):
            if A[i][k] == 1:
                v += 2 ** k
        if j == v:
            dp[i][j] = 1

        if dp[i][j] == INF:
            continue
    
        if i == M - 1:
            continue

        nv = 0
        for k in range(N):
            if A[i + 1][k] == 1:
                nv += 2 ** k
        
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        dp[i + 1][j | nv] = min(dp[i + 1][j | nv], dp[i][j] + 1)

if dp[-1][-1] == INF:
    print(-1)
else:
    print(dp[-1][-1])