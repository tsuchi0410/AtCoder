n, m = (int(x) for x in input().split())

d = {}
for i in range(m):
    a, b = (int(x) for x in input().split())
    
    if a in d:
        if d[a] != b:
            print('-1')
            exit()
    else:
        d[a] = b
        
l = [0] * n
for i in d:
    l[i-1] = d[i]
    
if n == 1 and len(l) == 1:
    if l[0] == 0:
        print(0)
        exit()
        
if l[0] == 0:
    print('-1')
    exit()


print(*l, sep = '')
