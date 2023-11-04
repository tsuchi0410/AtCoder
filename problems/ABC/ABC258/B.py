import numpy as np

N = int(input())

A = []
for i in range(N):
    num = int(input())
    x = [int(a) for a in str(num)]
    A.append(x)

ans = 0

# row
rowssum = map(sum, A)
cc = 0
aa = []
for i in rowssum:
    if ans < i:
        ans = max(ans, i)
        aa.append(A[cc])
    cc += 1
        

# col
cc = 0
colsum = map(sum, zip(*A))
for i in colsum:
    if ans < i:
        ans = max(ans, i)
        aa.append(zip(A[cc]))
    cc += 1


# naname1
B = np.array(A)
C = []
for i in range(N):
    C.append(np.roll(B[i],i))


cc = 0
colsum2 = map(sum, zip(*C))
for i in colsum2:
    if ans < i:
        ans = max(ans, i)
        aa.append(list(zip(C[cc])))
    cc += 1

# naname2
B2 = np.array(A)
C2 = []
for i in range(N):
    C2.append(np.roll(B2[i],-i))

cc = 0
colsum3 = map(sum, zip(*C2))
for i in colsum3:
    if ans < i:
        ans = max(ans, i)
        aa.append(list(zip(C2[cc])))
    cc += 1
  

print(ans)
print(aa)
