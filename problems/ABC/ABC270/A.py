a, b = (int(x) for x in input().split())

l = [0, 1, 2, 4]


l2 = []
fa = 0
fb = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            
            
            if a == l[i] + l[j] + l[k] and fa == 0:
                l2.append(l[i])
                l2.append(l[j])
                l2.append(l[k])
                fa = 1
            
            if b == l[i] + l[j] + l[k] and fb == 0:
                l2.append(l[i])
                l2.append(l[j])
                l2.append(l[k])
                fb = 1
            
            
ans = sum(list(set(l2)))
print(ans)
