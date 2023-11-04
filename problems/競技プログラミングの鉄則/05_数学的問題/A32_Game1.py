N, A, B = map(int, input().split())
dp = [False] * (N + 1)
for i in range(N + 1):
    if i - A >= 0 and dp[i - A] == False:
        dp[i] = True
    if i - B >= 0 and dp[i - B] == False:
        dp[i] = True
if dp[-1] == True:
    print("First")
else:
    print("Second")