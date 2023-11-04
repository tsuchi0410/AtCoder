from collections import defaultdict
N, K = map(int,input().split())
A = list(map(int,input().split()))
for i in range(N):
    A[i] -= 1
d = defaultdict(int)
d[0] = 0
i = 0
cnt = 0
while True:
    if A[i] in d:
        t = [d[A[i]], cnt]
        break
    else:
        d[A[i]] = cnt + 1
    i = A[i]
    cnt += 1

loop = []
f = False
for k, v in d.items():
    if t[0] == v:
        f = True
    if f == True:
        loop.append(k)

if K <= t[0]:
    for k, v in d.items():
        if v == K:
            print(k + 1)
else:
    K -= t[0]
    K %= t[1] - t[0] + 1    
    print(loop[K] + 1)