from collections import defaultdict
import itertools

N = int(input())
S = [input() for _ in range(N)]

d = defaultdict(int)
for i in range(N):
    
    name = S[i][0]
    d[name] += 1

l = []
for i in d:
    if i == 'M' or i == 'A' or i == 'R' or i == 'C' or i == 'H':
        l.append(d[i])
    

if len(l) < 3:
    print('0')
    exit()

a = 0
l2 = list(itertools.combinations(l, 3))

for i in l2:
    r = 1
    for j in i:
        r *= j
    
    a += r

print(a)    