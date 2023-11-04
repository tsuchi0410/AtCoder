N, K = map(int, input().split())
MOD = 10**9 + 7
ans = 0
# 足した数字の個数をカウント
# i 個の数字を使用
for i in range(K, N + 2):
    min_sum = i * (0 + i - 1) // 2
    max_sum = i * (N + (N - i + 1)) // 2
    ans += max_sum - min_sum + 1
    ans %= MOD
print(ans)