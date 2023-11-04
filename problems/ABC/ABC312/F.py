
N, M = map(int, input().split())
T0 = []
T1 = []
key = {}
for _ in range(N):
    t, x = map(int, input().split())
    if t == 0:
        T0.append(x)
    elif t == 1:
        T1.append(x)
    else:
        key.add(x)

