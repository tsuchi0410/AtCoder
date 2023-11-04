INF = 10**18
N, M = map(int,input().split())
cost = [[INF] * N for _ in range(N)]
dic = {}
for _ in range(M):
    a, b, c = map(int,input().split())
    a -= 1
    b -= 1
    cost[a][b] = c
    cost[b][a] = c
    dic[(a, b)] = c

for i in range(N):
    cost[i][i] = 0

for k in range(N):  # k 以下の都市を通るときの全点対最短経路
    for i in range(N):
        for j in range(N):
            if cost[i][k] != INF and cost[k][j] != INF:
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

cnt = 0
for k, v in dic.items():
    if cost[k[0]][k[1]] < v:
        cnt += 1
print(cnt)