A = list(map(int,input().split()))

L = []
for i in range(4):
    L.append([0]*len(A))
    L[0][i] = A[i]

for i in range(1,4):
    for j in range(4):
        if j == 0:
            L[i][j] = L[i-1][j]+L[i-1][j+1]
        elif j >= 1 and 2 >= j:
            L[i][j]  = L[i-1][j-1]+L[i-1][j]+L[i-1][j+1]
        else:
            L[i][j] = L[i-1][j-1]+L[i-1][j]

print(L[-1][-1])
        