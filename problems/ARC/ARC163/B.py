import bisect
from itertools import*

N, M = map(int, input().split())
A = list(map(int, input().split()))

A1 = A[0]
A2 = A[1]
A = A[2:]
A.sort()
L = [[k,len(list(v))] for k,v in groupby(A)]
cnt = 0
cmb = []
l = 0

for r in range(len(L)):
    k = L[r][0]
    v = L[r][1]
    cnt += v
    if cnt >= M:
        while True:
            if cnt >= M:
                cmb.append([l, r])
                cnt -= L[l][1]
                l += 1
            else:
                break
            if l == len(L) - 1:
                break

ans = 10**18
for i, j in cmb:
    cnt = 0
    l = L[i][0]
    r = L[j][0]
    if A1 > l:
        cnt += abs(A1 - l)
    if r > A2:
        cnt += abs(r - A2)
    ans = min(ans, cnt)

print(ans)