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
g = [[] for _ in range(n)]
for i in range(m):
    a, b = list(map(int,input().split()))
    a -= 1
    b -= 1
    # 有向グラフ
    g[a].append(b)
    # 無向グラフ
    g[b].append(a)

seen = [False] * n

# 0から判定
count = 1
rec(0, seen)

while (1):
    f = 0
    for i in range(n):
        if seen[i] == False:
            count += 1
            f = 1
            rec(i, seen)
        
    if f == 0:
        print(count)
        exit()    


