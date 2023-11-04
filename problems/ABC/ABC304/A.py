N = int(input())
L = []
A_min = 10**18
for _ in range(N):
    S, A = map(str,input().split())
    A = int(A)
    L.append([S, A])
    A_min = min(A_min, A)

ans = []
for i in range(N):
    if L[i][1] == A_min:
        for j in range(i, N):
            ans.append(L[j][0])
        for j in range(0, i):
            ans.append(L[j][0])
        break

for i in range(N):
    print(ans[i])