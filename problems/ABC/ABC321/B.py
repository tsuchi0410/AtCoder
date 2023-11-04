N, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

ans = 10**18

B = A[:N - 2]
if sum(B) >= X:
    ans = 0

B = A[1 : N - 1]
if sum(B) >= X:
    ans = min(ans, B[-1])

B = A[1 : N - 2]
if sum(B) <= X:
    if X - sum(B) <= A[-1]:
        ans = min(ans, X - sum(B))

if ans >= 101:
    print(-1)
else:
    print(ans)