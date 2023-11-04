N, M, K = map(int, input().split())
mod = 998244353

#inv = pow(M, -1, mod)
# 拡張ユークリッドの互除法を用いて、aの逆元を求める
def modinv(a, mod):
    b = mod
    x, y = 1, 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        x -= t * y
        x, y = y, x
    return (x + mod) % mod

inv = modinv(M, mod)

dp = [[0] * (N + 1) for _ in range(K + 1)]
dp[0][0] = 1
for i in range(K):
    for j in range(N):
        for k in range(1, M + 1):
            if j + k > N:
                over = j + k - N
                next = N - over
            else:
                next = j + k

            dp[i + 1][next] += dp[i][j] * inv
            dp[i + 1][next] %= mod

# K 回まで回すときにゴールする確率
ans = 0
for i in dp:
    ans += i[-1]
    ans %= mod

print(ans)