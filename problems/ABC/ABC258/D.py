n, x = (int(x) for x in input().split())
ab = []
for i in range(n):
    a, b = (int(x) for x in input().split())
    ab.append([a,b])

s = [0]
for i in range(n):
    s.append(s[i] + ab[i][0] + ab[i][1])

s = s[1:]
ans = float('inf')
for i in range(n):
    cnt = x - (i+1)
    if cnt < 0:
        break
    else:
        time = s[i] + cnt * ab[i][1]
        ans = min(ans, time)

print(ans)