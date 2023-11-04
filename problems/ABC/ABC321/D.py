import bisect

N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

SB = [0]
for i in range(M):
    SB.append(SB[i] + B[i])

ans = 0
for i in range(N):
    num = P - A[i]
    idx = bisect.bisect_left(B, num)
    ans += (len(B) - idx) * P + A[i] * idx + SB[idx]

print(ans)
