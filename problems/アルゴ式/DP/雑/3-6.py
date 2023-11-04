N, A, B = (int(x) for x in input().split())
X = list(map(int,input().split()))

dp = []
for i in range(N+1):
    dp.append([-1]*A)

dp[0][0] = 0
for i in range(N):
    for j in range(A):
        if dp[i][j] == -1:
            continue

        dp[i+1][j] = max(dp[i][j], dp[i+1][j])
        
        if j+X[i] <= A-1:
            dp[i+1][j+X[i]] += 1
        else:
            dp[i+1][(j+X[i]) % A] += 1

print("Yes" if dp[-1][B] >= 0 else "No")