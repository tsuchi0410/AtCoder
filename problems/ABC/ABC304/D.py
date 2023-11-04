import bisect
from collections import defaultdict
W, H = map(int,input().split())
N = int(input())
p = []
q = []
for _ in range(N):
    pp, qq = map(int,input().split())
    p.append(pp)
    q.append(qq)
A = int(input())
a = list(map(int,input().split()))
B = int(input())
b = list(map(int,input().split()))
a.sort()
b.sort()
dx = defaultdict(int)
dy = defaultdict(int)
for i in range(N):
    x = bisect.bisect_left(a, p[i])
    y = bisect.bisect_left(b, q[i])
    dx[(x, y)] += 1

ans_max = 0
ans_min = 10**18
for k, v in dx.items():
    ans_max = max(ans_max, v)
    ans_min = min(ans_min, v)

if len(dx) < (A + 1) * (B + 1):
    ans_min = 0
print(ans_min, ans_max)