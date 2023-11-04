from collections import defaultdict
h, w = (int(x) for x in input().split())

s = []
for i in range(h):
    s.append(input())

t = []
for i in range(h):
    t.append(input())

d = defaultdict(int)
for col in zip(*s):
    d[''.join(col)] += 1
    
for col in zip(*t):
    a = ''.join(col)
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