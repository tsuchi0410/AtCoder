import bisect
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans1 = []
ans2 = []
for i in range(N):
    idx = bisect.bisect_left(B, A[i])
    ans1.append(((i+1) + idx))

for i in range(M):
    idx = bisect.bisect_left(A, B[i])
    ans2.append(((i+1) + idx))

print(*ans1)
print(*ans2)
