N = int(input())
G = [input() for _ in range(N)]
A = []
for i in range(N):
    L = []
    for j in range(len(G[i])):
        if G[i][j] == "0":
            L.append(0)
        else:
            L.append(1)
    A.append(L)

L = []
for i in range(N):
    L.append(A[0][i])
for i in range(N):
    if i == 0:
        continue
    L.append(A[i][N - 1])
for i in range(N - 1, -1, -1):
    if i == N - 1:
        continue
    L.append(A[-1][i])
for i in range(N - 2, 0, -1):
    L.append(A[i][0])

buf = L[-1]
L = [buf] + L
L = L[:-1]

cnt = 0
for i in range(N):
    A[0][i] = L[cnt]
    cnt += 1
for i in range(N):
    if i == 0:
        continue
    A[i][N - 1] = L[cnt]
    cnt += 1
for i in range(N - 1, -1, -1):
    if i == N - 1:
        continue
    A[-1][i] = L[cnt]
    cnt += 1
for i in range(N - 2, 0, -1):
    A[i][0] = L[cnt]
    cnt += 1

for i in range(N):
    for j in range(N):
        A[i][j] = str(A[i][j])

for i in A:
    print("".join(i))