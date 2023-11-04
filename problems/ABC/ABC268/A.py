from collections import defaultdict
d = defaultdict(int)

l = list(map(int,input().split()))

for i in range(5):
    d[l[i]] += 1
    
print(len(d))