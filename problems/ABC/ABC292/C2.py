from collections import defaultdict
N = int(input())
d = defaultdict(int)
for A in range(1, N):
    for B in range(1, N):
        if A * B >= N:
            break
        else:
            d[A * B] += 1

ans = 0
for i in range(1, N):
    ans += d[i] * d[N - i]
print(ans)