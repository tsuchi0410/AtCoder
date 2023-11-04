n, k = (int(x) for x in input().split())
h = list(map(int,input().split()))

dp = [float('inf')] * n
dp[0] = 0
dp[1] = abs((h[1] - h[0]))


for i in range(2, n):
    for j in range(1, k+1):
        
        if i-j >= 0:
            dp[i] = min(dp[i], dp[i-j] + abs(h[i] - h[i-j]))

# print(dp)
print(dp[-1])   