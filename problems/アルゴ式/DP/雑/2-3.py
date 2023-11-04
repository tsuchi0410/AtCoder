N = int(input())
A = []
L = []
for i in range(N):
    A.append(list(map(int,input().split())))
    L.append([0]*3)

for i in range(3):
    L[0][i] = A[0][i]

for i in range(1,N):
    L[i][0] = A[i][0] + max(L[i-1][1], L[i-1][2])
    L[i][1] = A[i][1] + max(L[i-1][0], L[i-1][2])
    L[i][2] = A[i][2] + max(L[i-1][0], L[i-1][1])

print(max(L[N-1]))
    