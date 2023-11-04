H, W, K = map(int, input().split())
MOD = 1000000007

L = []
NUM = W - 1
for i in range(2 ** NUM):
    f = True
    l = [i >> j & 1 for j in range(NUM)]
    for j in range(NUM - 1):
        if l[j] == 1 and l[j + 1] == 1:
            f = False
    if f == True:
        L.append(l)

dp = [[0] * (W) for _ in range(H + 1)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        for k in L:
            # j 番目の bit が立っている -> 右に遷移
            if 0 <= j < W - 1 and k[j] == 1:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= MOD
            
            # j - 1 番目の bit が立っている -> 左に遷移
            elif 1 <= j and k[j - 1] == 1:
                dp[i + 1][j - 1] += dp[i][j]
                dp[i + 1][j - 1] %= MOD
            
            # どちらの bit も立っていない
            else:
                dp[i + 1][j] += dp[i][j]
                dp[i + 1][j] %= MOD

print(dp[-1][K - 1])