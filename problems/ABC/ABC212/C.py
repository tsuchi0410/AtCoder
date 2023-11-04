import bisect
N,M = (int(x) for x in input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A = sorted(A)
B = sorted(B)


ans = float('inf')
for i in range(N):
    
    if bisect.bisect_left(B,A[i]) >= len(B):
        ans = min(ans, abs(A[i]-(B[bisect.bisect_left(B,A[i])-1])))
    else:
        ans = min(ans, abs(A[i]-(B[bisect.bisect_left(B,A[i])-1])))
        ans = min(ans, abs(A[i]-(B[bisect.bisect_left(B,A[i])])))


print(ans)
