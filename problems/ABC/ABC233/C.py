N, X = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
L = []
for i in range(A[0][0]):
    L.append(A[0][i + 1])
for i in range(1, N):
    L2 = []
    for j in range(A[i][0]):
        for k in range(len(L)):
            L2.append(L[k] * A[i][j + 1])
    L = L2

print(L.count(X))
