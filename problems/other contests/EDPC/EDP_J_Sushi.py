N = int(input())
a = list(map(int, input().split()))

REP = 310
dp = [[[0] * (REP) for _ in range(REP)] for _ in range(REP)]
for k in range(REP):
    for j in range(REP):
        for i in range(REP):
            cnt = i + j + k
            if cnt == 0:
                continue
            if cnt > 310:
                continue
            tmp = N
            if i >= 1:
                tmp += dp[i - 1][j][k] * i
            if j >= 1 and i + 1 <= N:
                tmp += dp[i + 1][j - 1][k] * j
            if k >= 1 and j + 1 <= N:
                tmp += dp[i][j + 1][k - 1] * k
            tmp /= cnt
            dp[i][j][k] = tmp
            
print(dp[a.count(1)][a.count(2)][a.count(3)])