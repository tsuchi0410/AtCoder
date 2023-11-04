import bisect
N, M, D = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()

ans = -1
for i in range(N):
    vmin = bisect.bisect_left(B, A[i] - D)
    vmax  = bisect.bisect_right(B, A[i] + D)
    if vmin == vmax:
        continue
    else:
        v = B[vmax - 1]
        ans = A[i] + v

print(ans)