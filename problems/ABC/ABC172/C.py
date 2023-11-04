import bisect
n,m,k=(int(x) for x in input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

sa = [0];sb = [0]
for i in range(n):
    sa.append(sa[i] + a[i])
for i in range(m):
    sb.append(sb[i] + b[i])

ans = 0
for i in range(len(sa)):
    time = k - sa[i]
    if time < 0:
        break
    else:
        idx = bisect.bisect_right(sb, time) - 1
    ans = max(ans, i + idx)

print(ans)