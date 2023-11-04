from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
d = defaultdict(int)
ans = []
for i in range(3 * N):
    d[A[i]] += 1
    if d[A[i]] == 2:
        ans.append([i, A[i]])
l = []
for i in range(len(ans)):
    l.append(ans[i][1])

print(*l, sep = " ")