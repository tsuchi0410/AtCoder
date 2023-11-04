INF = 10**18
N = int(input())
X = [0] * N
Y = [0] * N
Z = [0] * N
for i in range(N):
    X[i], Y[i], Z[i] = map(int, input().split())

T = 0
A = 0
l = []
for i in range(N):
    if X[i] < Y[i]:
        p = (Y[i] - X[i]) // 2 + 1
        l.append([p, Z[i]])
        A += Z[i]
    else:
        T += Z[i]

rep = 10 ** 5 + 10
dp = [[INF] * rep for _ in range(len(l))]
for i in range(len(l)):
    for j in range(rep):
        p, z = l[i] 
        if j == z:
            dp[i][j] = min(dp[i][j], p)
        if dp[i][j] != INF and i + 1 < len(l):
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
            dp[i + 1][j + l[i + 1][1]] = min(dp[i + 1][j + l[i + 1][1]], dp[i][j] + l[i + 1][0])

if T > A:
    print(0)
    exit()
#print(dp)
ans = INF
for i in range(rep):
    if i + T > A - i:
        ans = min(ans, dp[-1][i])
print(ans)
