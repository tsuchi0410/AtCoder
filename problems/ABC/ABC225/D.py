from collections import deque
n, q = (int(x) for x in input().split())
l = []
for i in range(n + 1):
    l.append([False, False])

l[0][0] = -1; l[0][1] = -1
for i in range(q):
    qu = list(map(int,input().split()))
    if qu[0] == 1:
        l[qu[1]][1] = qu[2]
        l[qu[2]][0] = qu[1]
    elif qu[0] == 2:
        l[qu[1]][1] = False
        l[qu[2]][0] = False
    else:
        d = deque([qu[1]])
        next = l[qu[1]][1]
        # right
        while True:
            num = l[next][1]
            if num == -1:
                break
            elif num == False:
                d.append(next)
                break
            else:
                d.append(next)
                next = num
        # left
        next = l[qu[1]][0]
        while True:
            num = l[next][0]
            if num == -1:
                break
            elif num == False:
                d.appendleft(next)
                break
            else:
                d.appendleft(next)
                next = num
        
        print(len(d), *d)