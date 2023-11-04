N, K = map(int, input().split())
p = list(map(int, input().split()))
v = [0]
for i in range(1, 1001):
    a = 0
    for j in range(i):
        a += (j + 1) * (1 / i)
    v.append(a)
r = 0
ans = 0
a = 0
for l in range(N):
    a += v[p[l]]
    if l - r + 1 < K:
        continue
    if l - r + 1 > K:
        a -= v[p[r]]
        r += 1
    if l - r + 1 == K:
        ans = max(ans, a)
    
print(ans)