from collections import defaultdict
N, K = map(int, input().split())
A = list(map(int,input().split()))

S = [0]
for i in range(N):
    S.append(S[i] + A[i])

ans = 0
d = defaultdict(int)
for i in range(len(S)):
    ans += d[S[i] - K]
    d[S[i]] += 1
print(ans)