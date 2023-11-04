N = int(input())
A = list(map(int, input().split()))
ave = sum(A) // N
S = [ave] * N

diff = sum(A) - sum(S)
for i in range(diff):
    S[i] += 1

A.sort()
S.sort()
ans = 0
for i in range(N):
    ans += abs(S[i] - A[i])

print(ans // 2)