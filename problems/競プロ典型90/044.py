n, q = (int(x) for x in input().split())
a = list(map(int,input().split()))

cnt = 0
for i in range(q):
    t, x, y = (int(x) for x in input().split())
    if t == 1:
        idx_x = (x - cnt) % n - 1
        idx_y = (y - cnt) % n - 1
        a[idx_x], a[idx_y] = a[idx_y], a[idx_x]
    elif t == 2:
        cnt += 1
    else:
        idx = (x - cnt) % n - 1
        print(a[idx])