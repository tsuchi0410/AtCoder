k = int(input())
mod = 10 ** 9 + 7

dp = [0] * (k+1)
dp[0] = 1

for i in range(k+1):
    for j in range(1, 10):
        if i < j:
            continue
        dp[i] += dp[i-j]
        dp[i] %= mod

k = str(k)
res = 0
for i in range(len(k)):
    res += int(k[i])

if res % 9 == 0:
    print(dp[-1])
else:
    print(0)