n = int(input())
d = [list(map(int, input().split())) for _ in range(n - 1)]
dp = [[0] * (1 << n) for _ in range(n + 1)]
for i in range(n):
    for j in range(1 << n):
        if (j >> i) & 1:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            continue
        for k in range(i + 1, n):
            if (j >> k) & 1:
                continue
            dp[i + 1][j | (1 << k)] = max(dp[i + 1][j | (1 << k)], dp[i][j] + d[i][k - i - 1])

    for i in dp:
        print(i)
    print()
print(max(dp[n]))