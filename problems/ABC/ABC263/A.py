L = list(map(int,input().split()))

d = {}
for i in L:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1


f = 0
for myv in d.values():
    if myv == 2 or myv == 3:
        f = 1
    else:
        f = 0
        print("No")
        exit()

print("Yes")