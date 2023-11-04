n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

da = {}
db = {}
dc = {}
for i in range(46):
    da[i] = 0
    db[i] = 0
    dc[i] = 0

for i in range(n):
    da[a[i] % 46] += 1
    db[b[i] % 46] += 1
    dc[c[i] % 46] += 1

ans = 0
for i in da:
    for j in db:
        for k in dc:
            if (i + j + k) % 46 == 0:
                ans += da[i] * db[j] * dc[k]

print(ans)