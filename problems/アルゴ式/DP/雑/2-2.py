N = int(input())
A = list(map(int,input().split()))

L = []
for i in range(N):
    L.append([0]*N)
    L[0][i] = A[i]

for i in range(1,N):
    for j in range(N):
        L[i][j] += L[i-1][j]
        if j >= 1:
            L[i][j] += L[i-1][j-1]
        if N-1 > j:
            L[i][j] += L[i-1][j+1]
        
        L[i][j] = L[i][j] % 100

print(L[-1][-1])