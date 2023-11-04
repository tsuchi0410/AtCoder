n,m = (int(x) for x in input().split())
s = []
for i in range(n):
    s.append(input())

t = set()
for i in range(m):
    t.add(input())

ans = 0
for i in s:
    if i[3:] in t:
        ans += 1

print(ans)