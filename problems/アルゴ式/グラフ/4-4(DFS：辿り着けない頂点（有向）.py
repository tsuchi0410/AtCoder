import sys
sys.setrecursionlimit(10 ** 6)

def rec(v, l):
    # 頂点 v を黒く塗る
    l[v] = True
    # 頂点 v の頂点番号を出力する
    #print(v, end = ' ')
    
    for v2 in g[v]:
        if l[v2] == True: # 頂点v2がすでに塗られている
            continue    
        rec(v2, l)
    
        
n, m = (int(x) for x in input().split())
g = [[] for _ in range(m)]
for i in range(m):
    a, b = list(map(int,input().split()))
    
    # 有向グラフ
    g[a].append(b)
    # 無向グラフ
    # g[b].append(a)

l = [False] * n
rec(0, l)

print(l.count(False))