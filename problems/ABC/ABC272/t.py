import math
m = int(input())
k = int(math.sqrt(m))
v = []
for i in range(k+1):
    for j in range(i, k+1):
        
        if i**2 + j**2 == m:
            v.append([i, j])

for i in range(len(v)):
    print(v[i])
