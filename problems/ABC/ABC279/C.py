from collections import defaultdict
h, w = (int(x) for x in input().split())

s = []
for i in range(h):
    s.append(input())

t = []
for i in range(h):
    t.append(input())

s2 = []
for col in zip(*s):
    s2.append(col)

t2 = []
for col in zip(*t):
    t2.append(col)

d = defaultdict(int)
for i in s2:
    a = ''
    for j in i:
        if j == '#':
            a += '#'
        else:
            a += '.'
    d[a] += 1

for i in t2:
    a = ''
    for j in i:
        if j == '#':
            a += '#'
        else:
            a += '.'
    if a in d:
        if d[a] == 0:
            print('No')
            exit()
        else:
            d[a] -= 1
    else:
        print('No')
        exit()

print('Yes')