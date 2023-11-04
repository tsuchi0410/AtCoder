n = int(input())
a = list(map(int,input().split()))

d = {}
d2 = {}
a.sort(reverse = True)
for i in range(n):
    x = a[i] % 2
    d[i] = x
    d2[i] = a[i]



l = []
l2 = []
for i in d:
    if d[i] == 0:
        l.append(i)
    if d[i] == 1:
        l2.append(i)

    if len(l) == 2:
        e = d2[l[0]]+d2[l[1]]
    if len(l2) == 2:
        o = d2[l2[0]]+d2[l2[1]]
        
if len(l) >= 2 and len(l2) >= 2:
    print(max(e, o))
elif len(l) >= 2:
    print(e)
elif len(l2) >= 2:
    print(o)
else:
    print('-1')
    




