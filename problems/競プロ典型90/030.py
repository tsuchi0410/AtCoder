N, K = map(int, input().split())
cnt = [0] * (N + 1)
for i in range(2, N + 1):
    if cnt[i] == 0:
        j = i
        while j <= N:
            cnt[j] += 1
            j += i

ans = 0
for i in cnt:
    if i >= K:
        ans += 1
print(ans)