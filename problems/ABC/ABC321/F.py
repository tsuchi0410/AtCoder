from sortedcontainers import SortedList
MOD = 998244353

Q, K = map(int, input().split())
N = 50
dp = [[0] * N for _ in range(N)]
ans = []
for i in range(Q):
    op = list(input())
    num = "".join(op[2:])
    num = int(num)

    if op[0] == "-":
        for j in range(N):
            if j == num:
                dp[i][j] -= 1
            
            if i == Q - 1:
                continue

            if j - num >= 0:
                dp[i + 1][j - num] += dp[i][j]

    elif op[0] == "+":
        for j in range(N):
            if j == num:
                dp[i][j] += 1

            if i == Q - 1:
                continue

            dp[i + 1][j] += dp[i][j]

            if j + num < N:
                dp[i + 1][j + num] += dp[i][j]

    ans.append(dp[i][K])

print(ans)