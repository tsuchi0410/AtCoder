import sys
sys.setrecursionlimit(10**6)

def dfs(now):
    global path,ans
    path.add(now)
    ans += 1
    if ans == 10**6:
        print(ans)
        exit()

    for to in g[now]:
        if to not in path:
            dfs(to)
            
    path.remove(now)

n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    # 入力の受け取り
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

ans = 0
path = set()

dfs(0)
print(ans)