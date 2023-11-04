INF = 10**18
def ed(xa, ya, xb, yb):
    return ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5

N = int(input())
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

skip = 40
dp = [[INF] * skip for _ in range(N)]
for j in range(1, skip):
    if j < N:
        dp[j][j - 1] = ed(X[0], Y[0], X[j], Y[j])

for i in range(1, N - 1):
    for j in range(skip):
        for k in range(1, skip):
            if i + k < N and j + k - 1 < skip:
                d = ed(X[i], Y[i], X[i + k], Y[i + k])
                dp[i + k][j + k - 1] = min(dp[i + k][j + k - 1], dp[i][j] + d)

# for i in dp:
#     print(i)

ans = INF
for i in range(skip):
    if i == 0:
        ans = min(ans, dp[N - 1][i])
    else:
        ans = min(ans, dp[N - 1][i] + 2 ** (i - 1))
print(ans)