# 辺情報を表す構造体
class edge:
    def __init__(self, start, end, leng):
        self.start = start  # 辺の始点
        self.end = end      # 辺の終点
        self.leng = leng    # 辺の長さ

INF = 10**9 

# main
# 入力を受け取る
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    u, v, w = map(int, input().split())
    g[u].append(edge(u, v, w))

for v in range(n):
    dist = INF
    ans = -1
    
    for e in g[v]:
        if e.leng < dist:
            dist = e.leng
            ans = e.end
        
        elif e.leng == dist:
            ans = min(ans, e.end)
    
    print(ans)