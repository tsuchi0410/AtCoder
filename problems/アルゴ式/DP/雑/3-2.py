N, M = (int(x) for x in input().split())
W = list(map(int,input().split()))

dp = []
for i in range(N):
    dp.append([False]*(M+1))

# 初期値
for i in W:
    if i <= M:
        dp[0][i] = True

    if dp[0][M] == True:
        print("Yes")
        exit()

for i in range(1, N):
    for j in range(M+1):
        for k in range(len(W)):
            if j-W[k] >= 0 and dp[i-1][j-W[k]] == True:
                dp[i][j] = True

    if dp[i][M] == True:
        print("Yes")
        exit()

print("No")
