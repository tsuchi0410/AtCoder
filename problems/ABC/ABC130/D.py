import bisect
N, K = map(int, input().split())
A = list(map(int,input().split()))

S = [0]
for i in range(N):
    S.append(S[i] + A[i])

ans = 0
for i in range(N):
    idx = bisect.bisect_left(S, K + S[i])
    ans += len(S) - idx
    
print(ans)