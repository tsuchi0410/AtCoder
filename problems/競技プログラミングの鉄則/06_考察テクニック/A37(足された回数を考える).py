from collections import defaultdict
N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

L = defaultdict(int)
R = defaultdict(int)
for i in range(N):
    L[A[i]] += 1
for i in range(M):
    R[C[i]] += 1

ans = 0
for k, v in L.items():
    ans += k * v * M
for k, v in R.items():
    ans += k * v * N
ans += N * M * B
print(ans)