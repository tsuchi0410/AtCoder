H, W = (int(x) for x in input().split())
A = []
for i in range(H):
    g = list(map(int,input().split()))
    A.append(g)

B = []
for i in range(H):
    g = list(map(int,input().split()))
    B.append(g)

ans = 0
for i in range(H - 1):
    for j in range(W - 1):
        if A[i][j] != B[i][j]:
            cnt = B[i][j] - A[i][j]
            
            A[i][j] += cnt
            A[i][j + 1] += cnt
            A[i + 1][j] += cnt
            A[i + 1][j + 1] += cnt
            
            ans += abs(cnt)

if A == B:
    print("Yes")
    print(ans)
else:
    print("No")
