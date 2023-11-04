n = int(input())
li = [0] * (2 * 10 ** 5 + 1)
for i in range(n):
    l, r = (int(x) for x in input().split())
    li[l] += 1; li[r] -= 1

cnt = 0
ans = []
for i in range(len(li)):
    if li[i] > 0:
        if cnt == 0:
            ans.append(i)
        cnt += li[i]
    elif li[i] < 0:
        cnt += li[i]
        if cnt == 0:
            ans.append(i)

b = []
for i in ans:
    b.append(i)
    if len(b) == 2:
        print(*b)
        b = []

