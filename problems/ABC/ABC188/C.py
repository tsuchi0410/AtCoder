import copy
n = int(input())
a = list(map(int,input().split()))

d = {}
for i in range(2 ** n):
    d[a[i]] = i + 1

while len(a) != 2:

    l = []
    for i in range(0, len(a) - 1, 2):
        l.append(max(a[i], a[i+1]))
    a = copy.copy(l)


print(d[min(a[0],a[1])])

