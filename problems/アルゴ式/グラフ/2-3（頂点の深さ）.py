import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
P = list(map(int,input().split()))

def rec(v, p, d, chs):
    
    if not v == 0:
        # 子頂点の深さ = 親頂点の深さ + 1
        p += 1
        d[v] = p 
    
    for ch in chs[v]:
        rec(ch, p, d, chs)

        
chs = [[] for _ in range(N)]
for i in range(N-1):
    chs[P[i]].append(i+1)

# rec(根頂点, 親頂点, 深さリスト, 子頂点リスト)
d = [0] * N
rec(0, 0, d, chs)
print(*d, sep = '\n')