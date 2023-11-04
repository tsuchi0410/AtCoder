N, M = map(int,input().split())
X = list(map(int,input().split()))
x_min = min(X)
if x_min < 0:
    for i in range(M):
        X[i] += abs(x_min)
if x_min > 0:
    for i in range(M):
        X[i] -= x_min
X.sort()
L = []
for i in range(1, M):
    L.append(X[i] - X[i - 1])
L.sort(reverse=True)
ans = 0
for i in range(N - 1, len(L)):
    ans += L[i]
print(ans)