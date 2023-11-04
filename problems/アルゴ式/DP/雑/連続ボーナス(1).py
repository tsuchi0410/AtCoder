N, A = map(int, input().split())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
R = list(map(int,input().split()))
S = [P, Q, R]
INF = float("inf")

dp = [[INF] * 3 for _ in range(N)]
for i in range(3):
    dp[0][i] = S[i][0]

for i in range(N):
    for j in range(3):
        for k in range(3):
            if i == N - 1:
                continue
            if j == k:
                dp[i + 1][k] = min(dp[i + 1][k], dp[i][k] + S[k][i + 1] - A)
            else:
                dp[i + 1][k] = min(dp[i + 1][k], dp[i][j] + S[k][i + 1])

print(min(dp[-1]))
