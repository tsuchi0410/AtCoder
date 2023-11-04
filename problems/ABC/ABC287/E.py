import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)

N = int(input())
S = [input() for _ in range(N)]

ans = [0] * (N)

def search(l, idx):
    d = defaultdict(list)
    for i in range(len(l)):
        if len(S[l[i]]) > idx:
            d[S[l[i]][idx]].append(l[i])
        else:
            ans[l[i]] = idx
    if len(d) > 0:
        for v in d.values():
            if len(v) == 1:
                ans[v[0]] = idx
            else:
                search(v, idx + 1)

table = defaultdict(list)
for i in range(N):
    table[S[i][0]].append(i)

idx = 0
for v in table.values():
    if len(v) == 1:
        ans[v[0]] = 0
    else:
        search(v, idx + 1)

print(*ans, sep = "\n")