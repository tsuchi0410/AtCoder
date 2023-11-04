from collections import deque
N, M = map(int, input().split())
G = [[] for _ in range(N)]  # グラフを表現する隣接リスト (終点のインデックスから、始点の番号を取り出す)
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)

ans = 0
for node in range(N):
    queue = deque([node])
    
    d = [-1] * N
    d[node] = 0
    
    while queue:
        v = queue.popleft()
        for i in G[v]:
            if d[i] == -1:
                d[i] = d[v] + 1
                queue.append(i)

    for i in range(N):
        if d[i] >= 2:
            ans += 1

print(ans)