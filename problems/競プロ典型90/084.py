import bisect
n=int(input())
s=input()

o = []
x = []
for i in range(n):
    if s[i] == 'o':
        o.append(i)
    else:
        x.append(i)
ans = 0
for i in range(n):
    if s[i] == 'o':
        idx = bisect.bisect_left(x, i)
        if idx == len(x):
            continue
        ans += n - x[idx]
    else:
        idx = bisect.bisect_left(o, i)
        if idx == len(o):
            continue
        ans += n - o[idx]

print(ans)