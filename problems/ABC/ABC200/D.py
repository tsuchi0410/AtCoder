N = int(input())
A = list(map(int, input().split()))

if N >= 8:
    A = A[:8]

dic = {}
NUM = len(A)
for i in range(2 ** NUM):
    l = [i >> j & 1 for j in range(NUM)]
    if l.count(1) == 0:
        continue
    cnt = 0
    for j in range(len(l)):
        if l[j] == 1:
            cnt += A[j] % 200
    cnt %= 200
    if cnt in dic:
        print("Yes")
        ans = [dic[cnt].count(1)]
        for i, k in enumerate(dic[cnt]):
            if k == 1:
                ans.append(i + 1)
        print(*ans)
        ans = [l.count(1)]
        for i, k in enumerate(l):
            if k == 1:
                ans.append(i + 1)
        print(*ans)
        exit()
    else:
        dic[cnt] = l

print("No")