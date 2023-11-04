n,a,b = (int(x) for x in input().split())
s = input()
ans = float("inf")
for i in range(n):

    j = 0
    k = -1
    cnt = 0
    while j != n // 2:
        if s[j] != s[k]:
            cnt += 1
        j += 1
        k -= 1

    ans = min(ans, (i)*a + b*cnt)
    s = s[1:] + s[0]

print(ans)