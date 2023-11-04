import numpy as np
N = int(input())
A = []
for i in range(N):
    A.append(list(map(int,input().split())))
B = []
for i in range(N):
    B.append(list(map(int,input().split())))

A = np.array(A)
B = np.array(B)

for _ in range(4):
    f = True
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                if B[i][j] != 1:
                    f = False
    if f == True:
        print("Yes")
        exit()
    
    A = np.rot90(A)

print("No")