n, m = (int(x) for x in input().split())
a = list(map(int,input().split()))

s = sum(a)
a.sort()
a = a + a

cnt = a[0]
ans = float('inf')
for i in range(len(a) - 1):
    if a[i+1] == (a[i] + 1) % m or a[i+1] == a[i]:
        cnt += a[i+1]
    else:
        ans = min(ans, s - cnt)
        cnt = a[i+1]

if ans == float('inf'):
    print(0)
else:
    print(ans)