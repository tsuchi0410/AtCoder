N = int(input())
l = []
for i in range(60):
    if (N >> i) & 1 == 1:
        l.append(1 << i)

for i in range(1 << len(l)):
    ans = 0
    
    for j in range(len(l)):
        
        if (i >> j) & 1 == 1:
            ans += l[j]
    
    print(ans)
