N, K = map(int,input().split())
ans = 0
for i in range(1, N + 1):
    now = i
    cnt = 1 / N
    while now < K:
        now *= 2
        cnt *= (1 / 2)
    ans += cnt
print(ans)