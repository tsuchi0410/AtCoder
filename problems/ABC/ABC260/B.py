N, X, Y, Z = (int(x) for x in input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A2 = []
B2 = []
C2 = []
ans = []
for i in range(len(A)):
    A2.append([A[i],0])
    B2.append([B[i],0])
    C2.append([A[i]+B[i],0])
    

num = -1
recnum = -1
for i in range(X):
    for j in range(len(A)):
        if A2[j][1] == 0:
            if num < A[j]:
                num = A[j]
                recnum = j
    
    A2[recnum][1] = 1
    num = -1
    recnum = -1

for i in range(len(A)):
    if A2[i][1] == 1:
        ans.append(i+1)

num = -1
recnum = -1
for i in range(Y):
    for j in range(len(B)):
        if A2[j][1] == 0 and B2[j][1] == 0:
            if num < B[j]:
                num = B[j]
                recnum = j
    
    B2[recnum][1] = 1
    num = -1
    recnum = -1

for i in range(len(B)):
    if B2[i][1] == 1:
        ans.append(i+1)
    
num = -1
recnum = -1
for i in range(Z):
    for j in range(len(C2)):
        if A2[j][1] == 0 and B2[j][1] == 0 and C2[j][1] == 0:
            if num < A[j]+B[j]:
                num = A[j]+B[j]
                recnum = j
    
    C2[recnum][1] = 1
    num = -1
    recnum = -1


for i in range(len(C2)):
    if C2[i][1] == 1:
        ans.append(i+1)

ans = sorted(ans)
for i in range(len(ans)):
    print(ans[i])


