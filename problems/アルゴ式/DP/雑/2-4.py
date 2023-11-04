N = int(input())

L = []
for i in range(N):
    L.append([0]*N)

L[0][0] = 1
for i in range(N):
    for j in range(N):
        if i-1 >= 0:
            L[i][j] += L[i-1][j]
        if j-1 >= 0:
            L[i][j] += L[i][j-1]

print(L[-1][-1])
print(L)