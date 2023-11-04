from collections import defaultdict
H,W,N = (int(x) for x in input().split())

A = []
B = []
for i in range(N):
    a,b = (int(x) for x in input().split())
    A.append(a)
    B.append(b)

Asort = list(set(sorted(A)))
Bsort = list(set(sorted(B)))

da = defaultdict(int)
db = defaultdict(int)
ca = 1
cb = 1
for i in range(len(Asort)):
    da[Asort[i]] = ca
    ca += 1
for i in range(len(Bsort)):
    db[Bsort[i]] = cb
    cb += 1

# da 列　db 行
for i in range(N):
    print(da[A[i]], db[B[i]])

