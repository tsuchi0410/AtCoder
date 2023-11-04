N, M = map(int, input().split())
A = list(map(int, input().split()))

A1 = A[0]
A2 = A[1]
A = A[2:]
A.sort()
ans = 10 ** 18
for i in range(len(A)):
    l = i
    r = i + M - 1
    if r >= len(A):
        break
    cnt = 0
    if A1 > A[l]:
        cnt += abs(A1 - A[l])
    if A[r] > A2:
        cnt += abs(A2 - A[r])
    ans = min(ans, cnt)

print(ans)