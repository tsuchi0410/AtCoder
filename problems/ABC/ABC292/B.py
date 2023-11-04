from collections import defaultdict
N, Q = map(int, input().split())
d = defaultdict(int)
for i in range(Q):
    num, x = map(int, input().split())
    if num == 1:
        d[x] += 1
    elif num == 2:
        d[x] += 2
    else:
        if d[x] >= 2:
            print("Yes")
        else:
            print("No")