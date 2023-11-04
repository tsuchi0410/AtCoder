import bisect
N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
for i in range(1, N + 1):
    idx = bisect.bisect_left(A, i)
    num = A[idx] - i
    print(num)