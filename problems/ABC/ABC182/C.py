N = list(input())
NUM = len(N)
ans = 10**18
for i in range(2 ** NUM):
    l = [i >> j & 1 for j in range(NUM)]
    cnt = 0
    for j in range(len(l)):
        if l[j] == 0:
            cnt += int(N[j])

    if l.count(0) == 0:
        continue

    if cnt % 3 == 0:
        ans = min(ans, l.count(1))

if ans == 10**18:
    print(-1)
else:
    print(ans)