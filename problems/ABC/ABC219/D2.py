n = int(input())
x, y = (int(x) for x in input().split())
ab = []
for i in range(n):
    a, b = (int(x) for x in input().split())
    ab.append([a, b])

inf = float('inf')
dp = [[inf] * (y+1) for _ in range(x+1)]
dp[0][0] = 0
for i in range(n):
    # 後ろから更新しないとDPできない
    for j in range(x, -1, -1):
        for k in range(y, -1, -1):
            if dp[j][k] < inf:
                jj = min(j+ab[i][0], x)
                kk = min(k+ab[i][1], y)
                dp[jj][kk] = min(dp[jj][kk], dp[j][k] + 1)

if dp[-1][-1] == inf:
    print(-1)
else:
    print(dp[-1][-1])
