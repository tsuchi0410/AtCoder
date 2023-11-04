INF = 10**18

def warshall_floyd():

    for k in range(N):  # k 以下の都市を通るときの全点対最短経路
        for i in range(N):
            for j in range(N):
                if cost[i][k] != INF and cost[k][j] != INF:
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

    return cost

N, K = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(N)]
cost = [[INF] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if a[i][j] == 1:
            cost[i][j] = 1
    # cost[i][i] = 0
        
dist = warshall_floyd()
Q = int(input())
for _ in range(Q):
    s, t = map(int,input().split())
    s -= 1
    t -= 1
    s %= N
    t %= N
    print(-1) if dist[s][t] == INF else print(dist[s][t])
    