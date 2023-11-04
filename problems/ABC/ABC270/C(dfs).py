import sys
sys.setrecursionlimit(10 ** 6)

def rec(v, seen, prev):
    # 頂点 v を黒く塗る
    seen[v] = True
    # 頂点 v の頂点番号を出力する
    # print(v, end = ' ')
    
    for v2 in g[v]:
        if seen[v2] == True: # 頂点v2がすでに塗られている
            continue
        
        # どこからきたかを記録
        prev[v2] = v
        rec(v2, seen, prev)
        

        
n, x, y = (int(x) for x in input().split())
g = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = list(map(int,input().split()))
    
    # 有向グラフ
    g[a].append(b)
    # 無向グラフ
    g[b].append(a)

seen = [False] * (n+1)
prev = [-1 for _ in range(n+1)]
rec(x, seen, prev)

print(g)
print(prev)

ans = [y]
while (1):
    a = prev[y]
    
    if a == x:
        ans.append(a)
        break
    else:
        ans.append(a)
        y = a

ans.reverse()
print(*ans, sep=' ')
