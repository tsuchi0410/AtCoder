import math
N = int(input())
cnt = 0
for i in range(3, 10):
    if N <= 10 ** i - 1:
        N /= 10 ** cnt
        ans = math.floor(N) * (10 ** cnt)
        print(ans)
        exit()
    cnt += 1