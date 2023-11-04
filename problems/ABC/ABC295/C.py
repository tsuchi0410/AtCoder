from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)
ans = 0
for i in range(N):
    d[A[i]] += 1
    if d[A[i]] % 2 == 0:
        ans += 1

print(ans)