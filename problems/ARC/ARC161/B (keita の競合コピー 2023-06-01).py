import bisect
L = []
for i in range(0, 60):
    for j in range(i + 1, 60):
        for k in range(j + 1, 60):
            L.append(2**i + 2**j + 2**k)
L.sort()
T = int(input())
for _ in range(T):
    N = int(input())
    idx = bisect.bisect_right(L, N)
    if idx == 0:
        print(-1)
    else:
        print(L[idx - 1])