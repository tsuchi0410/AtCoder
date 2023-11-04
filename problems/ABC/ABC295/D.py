from collections import defaultdict
S = input()
N = len(S)


d = defaultdict(int)
L = [0] * 10
d[tuple(L)] += 1
for i in range(N):
    L[int(S[i])] += 1    
    L[int(S[i])] %= 2 
    d[tuple(L)] += 1

ans = 0
for v in d.values():
    if v >= 2:
        ans += v * (v - 1) // 2
print(ans)
