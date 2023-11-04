n, k = (int(x) for x in input().split())
l = []
dp = [[0] * 3 for _ in range(n)]

for i in range(k):
    a, b = (int(x) for x in input().split())
    a -= 1; b -= 1
    for j in range(3):
        if j != b:
            dp[a][j] = None

# １日目
a = 0
for i in range(3):
    if dp[0][i] != None:
        dp[0][i] = 1
        a += 1

# ２日目
for i in range(3):
    if dp[1][i] != None:
        dp[1][i] = a            

for i in range(2, n):
    for j in range(3):

        if dp[i][j] != None:
            

for i in dp:
    print(i)