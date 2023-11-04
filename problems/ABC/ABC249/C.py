import itertools
from collections import defaultdict

N, K = (int(x) for x in input().split())
S = []
for i in range(N):
    S.append(input())

ans = 0
for i in range(1, N + 1):
    l = list(itertools.combinations(S, i))
    
    for j in l:
        s = list("".join(j))

        d = defaultdict(int)
        for k in s:
            d[k] += 1
        
        res = 0
        for k in d:
            if d[k] == K:
                res += 1

        ans = max(ans, res)

print(ans)

