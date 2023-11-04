n = int(input())
a = list(map(int,input().split()))
s = [0]
m = [0]
for i in range(n):
    s.append(s[i]+a[i])
    if a[i] > m[i]:
        m.append(a[i])
    else:
        m.append(m[i])

p = 0
ans = 0
for i in range(len(s)):
    p = p + m[i+1]
    ans = max(ans, p)
    p = p + s[i]
    print(p)

print(ans)