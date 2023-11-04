n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
x = int(input())

b = set(b)
dp = [False] * (10**5 + 10)

for i in b:
    dp[i] = -1

dp[0] = True
for i in range(len(dp)):
    for j in range(n):
        if i + a[j] < len(dp) and dp[i] == True:
            if dp[i + a[j]] != -1:
                dp[i + a[j]] = True

if dp[x] == True:
    print("Yes")
else:
    print("No")