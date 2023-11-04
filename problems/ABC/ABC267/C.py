N, M = (int(x) for x in input().split())
A = list(map(int,input().split()))

S = [0]
for i in range(0, N):
    S.append(S[i] + A[i])

ans = 0
for i in range(0, M):
    ans += (i + 1) * A[i]

x = ans
for i in range(M, N):
    
    res = x - (S[i] - S[i-M]) + A[i] * M
    ans = max(ans, res)
    x = res

print(ans)
