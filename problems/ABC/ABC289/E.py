t = int(input())

for i in range(t):
    n, m = (int(x) for x in input().split())
    g = [[] for _ in range(n)]
    c = list(map(int,input().split()))
    for j in range(m):
        a, b = (int(x) for x in input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    
    