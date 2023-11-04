n,C=(int(x) for x in input().split())

event = []
for i in range(n):
    a, b, c = (int(x) for x in input().split())
    event.append([a - 1, c])
    event.append([b, -c])

event.sort()
cnt = 0
ans = 0
pre_day = 0
for day, cost in event:
    if pre_day != day:
        ans += min(cnt, C) * (day - pre_day)
        pre_day = day
    cnt += cost

print(ans)