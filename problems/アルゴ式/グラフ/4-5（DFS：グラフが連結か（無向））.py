import sys
sys.setrecursionlimit(10 ** 6)

def rec(v, seen):
    # 頂点 v を黒く塗る
    seen[v] = True
    # 頂点 v の頂点番号を出力する
    # print(v, end = ' ')
    for v2 in g[v]:
        if seen[v2] == True: # 頂点v2がすでに塗られている
            continue    
        rec(v2, seen)
    
        
n, m = (int(x) for x in input().split())
g = [[] for _ in range(m)]
for i in range(m):
    a, b = list(map(int,input().split()))
    
    # 有向グラフ
    g[a].append(b)
    # 無向グラフ
    g[b].append(a)

seen = [False] * n
rec(0, seen)

if False in seen:
    print('No')
else:
    print('Yes')