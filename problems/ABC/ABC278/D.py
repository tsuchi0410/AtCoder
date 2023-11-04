from collections import defaultdict
n = int(input())
a = list(map(int,input().split()))
q = int(input())
x = 0
f = 0
d = defaultdict(int)
for i in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        d = defaultdict(int)
        f = 1
        x = query[1]
    elif query[0] == 2:
        d[query[1]] += query[2]

    elif query[0] == 3:
        if f == 0:
            if query[1] in d:
                print(d[query[1]] + a[query[1]-1])
            else:
                print(a[query[1]-1])
        else:
            if query[1] in d:
                print(x + d[query[1]])
            else:
                print(x)

