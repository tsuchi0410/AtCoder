N, K = map(int, input().split())
x = list(map(int, input().split()))
ans = 10**18
if K == 1:
    for i in range(N):
        ans = min(ans, abs(x[i]))
else:
    start = 0
    shift = min(x)
    if shift < 0:
        start = abs(shift)
        for i in range(N):
            x[i] += abs(shift)

    l = 0
    for r in range(K - 1, N):
        dist = x[r] - x[l]
        if x[l] <= start <= x[r]:
            ans = min(ans, dist + min(start - x[l], x[r] - start))
        elif start < x[l]:
            ans = min(ans, dist + (x[l] - start))
        elif x[r] < start:
            ans = min(ans, dist + (start - x[r]))
        l += 1
print(ans)