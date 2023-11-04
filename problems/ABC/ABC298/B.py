import copy
N = int(input())
A = []
for i in range(N):
    A.append(list(map(int,input().split())))
B = []
for i in range(N):
    B.append(list(map(int,input().split())))

f = True
for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            if B[i][j] != 1:
                f = False
if f == True:
    print("Yes")
    exit()      

L = copy.deepcopy(A)
for i in range(N):
    for j in range(N):
        L[j][N-1-i] = A[i][j]
f = True
for i in range(N):
    for j in range(N):
        if L[i][j] == 1:
            if B[i][j] != 1:
                f = False
if f == True:
    print("Yes")
    exit()            

L2 = copy.deepcopy(L)
for i in range(N):
    for j in range(N):
        L2[j][N-1-i] = L[i][j]
f = True
for i in range(N):
    for j in range(N):
        if L2[i][j] == 1:
            if B[i][j] != 1:
                f = False
if f == True:
    print("Yes")
    exit()     

L3 = copy.deepcopy(L2)
for i in range(N):
    for j in range(N):
        L3[j][N-1-i] = L2[i][j]
f = True
for i in range(N):
    for j in range(N):
        if L3[i][j] == 1:
            if B[i][j] != 1:
                f = False
if f == True:
    print("Yes")
    exit()

print("No")