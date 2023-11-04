import itertools
N = int(input())
XY = []
for i in range(N):
    a,b = (int(x) for x in input().split())
    XY.append([a,b])

l = list(itertools.combinations(XY,3))
cnt = 0
for i in l:
    # print(i)
    try:
        #01
        n1 = abs((i[1][1]-i[0][1]) / (i[1][0]-i[0][0]))
    except ZeroDivisionError:
        n1 = 0
    try: 
        #02
        n2 = abs((i[2][1]-i[0][1]) / (i[2][0]-i[0][0]))
    except ZeroDivisionError:
        n2 = 0
    try:
        #21
        n3 = abs((i[2][1]-i[1][1]) / (i[2][0]-i[1][0]))
    except ZeroDivisionError:
        n3 = 0

    if n1 == n2 and n1 == n3:
        cnt += 1

print(len(l)-cnt)


           
