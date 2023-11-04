n, d = (int(x) for x in input().split())
di = {}
lr = []
for i in range(n):
    l, r = (int(x) for x in input().split())
    di[l, r] = 0
    lr.append([l, r])

lr = sorted(lr, key=lambda x: x[1])
x = lr[0][1] + d - 1
ans = 1
for i in range(n-1):
    if lr[i+1][0] <= x:
        continue
    else:
        x = lr[i+1][1] + d - 1
        ans += 1

print(ans)