N, M = map(int,input().split())
A = [0] + [N + 1] + list(map(int,input().split())) 
A.sort()
L = []
for i in range(1, len(A)):
    if A[i] - A[i - 1] - 1 != 0:
        L.append(A[i] - A[i - 1] - 1)

# 白色のマスが存在しない
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