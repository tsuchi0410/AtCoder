n, k = (int(x) for x in input().split())
l = []
for i in range(n):
    a, b = (int(x) for x in input().split())
    l.append(b)
    l.append(a - b)

l.sort(reverse = True)
ans = 0
for i in range(k):
    ans += l[i]
print(ans)
