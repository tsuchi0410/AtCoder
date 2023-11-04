N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
dp = [0] * (N)
A = [0] + A
B = [0] * 2 + B
dp[1] = A[1]
for i in range(2, N):
    dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i])

print(dp[-1])