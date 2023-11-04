N = int(input())

L = []
for i in range(N):
    L.append([0]*N)

L[0][0] = 1
for i in range(N):
    for j in range(N):
        if i < N-1:
            L[i+1][j] += L[i][j]
        if j < N-1:
            L[i][j+1] += L[i][j]

print(L[-1][-1])