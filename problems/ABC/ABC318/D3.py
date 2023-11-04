N = int(input())
D = [list(map(int, input().split())) for _ in range(N - 1)]

dp = [0] * (1 << N)
for s in range(1 << N):
    for i in range(N - 1):
        if s >> i & 1:
            continue
        for j in range(len(D[i])):
            if s >> j & 1:
                continue
            t = s | 1 << i | 1 << j
            dp[t] = max(dp[t], dp[s] + D[i][j])
    
    print(dp)

