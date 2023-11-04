N, M = map(int, input().split())
A = list(map(int, input().split()))
T = [0,2,5,5,4,5,6,3,7,6]
dp = [""] * (N + 1)
# 初期値
for i in A:
    if T[i] <= N:
        dp[T[i]] = max(dp[T[i]], str(i))

for i in range(N + 1):
    if len(dp[i]) >= 1:
        for j in A:
            if i + T[j] <= N:
                if(len(dp[i]) + 1 > len(dp[i + T[j]])):
                    dp[i + T[j]] = dp[i] + str(j)
                elif(len(dp[i]) + 1 == len(dp[i + T[j]])):
                    dp[i + T[j]] = max(dp[i + T[j]], dp[i] + str(j))

print(dp[N])