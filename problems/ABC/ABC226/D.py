import math
import functools
n = int(input())
l = []
for i in range(n):
    a, b = (int(x) for x in input().split())
    l.append([a, b])
    
s = set()
ans = list()
for i in l:
    for j in l:
        if i == j:
            continue
        else:
            x = j[0]-i[0]
            y = j[1]-i[1]
            g = math.gcd(x, y)
            s.add(tuple([x // g, y // g]))
print(len(s))