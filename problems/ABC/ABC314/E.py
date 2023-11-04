N, M = map(int, input().split())
C = [0] * N
P = [0] * N
S = [0] * N
for i in range(N):
    C[i], P[i], *S[i] = map(int, input().split())

zero = [0] * N
for i in range(N):
    cnt = S[i].count(0)
    if cnt > 0:
        C[i] *= (P[i] / (P[i] - cnt))
        zero[i] += cnt

dp = [0] * (M + 110)
for i in range(M - 1, -1, -1):
    num = 10**18
    for j in range(N):
        cnt = 0
        for k in range(P[j]):
            cnt += dp[i + S[j][k]]
        cnt /= (P[j] - zero[j])
        cnt += C[j]
        num = min(num, cnt)
    dp[i] = num
    

print(dp[0])