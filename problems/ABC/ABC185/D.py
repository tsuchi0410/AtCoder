N, M = map(int,input().split())
A = list(map(int,input().split()))

if len(A) == 0:
    print(1)
    exit()

A.sort()
L = []
for i in range(M):
    if i == 0:
        if A[i] - 1 != 0:
            L.append(A[i] - 1)
    else:
        if A[i] - A[i - 1] - 1 != 0:
            L.append(A[i] - A[i - 1] - 1)
if A[-1] != N:
    L.append(N - A[-1])

if len(L) == 0:
    print(0)
    exit()

k = min(L)
ans = 0
for i in range(len(L)):
    if L[i] % k == 0:
        ans += L[i] // k
    else:
        ans += L[i] // k + 1

print(ans)
