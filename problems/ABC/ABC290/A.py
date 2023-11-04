n, m = (int(x) for x in input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
for i in range(m):
    ans += a[b[i] - 1]
print(ans)