N, K = map(int, input().split())
a = list(map(int, input().split()))
dp = [False] * (N + 1)
for i in range(N + 1):
    for j in range(K):
        if i - a[j] >= 0 and dp[i - a[j]] == False:
            dp[i] = True
if dp[-1] == True:
    print("First")
else:
    print("Second")