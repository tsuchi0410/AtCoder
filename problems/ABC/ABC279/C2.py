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

print(s2)
s2.sort()
t2.sort()
print('Yes') if s2 == t2 else print('No')
