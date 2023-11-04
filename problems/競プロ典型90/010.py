n = int(input())
c1 = []
c2 = []
for i in range(n):
    c, p = (int(x) for x in input().split())
    if c == 1:
        c1.append(p)
        c2.append(0)
    else:
        c1.append(0)
        c2.append(p)

s1 = [0]
for i in range(0, len(c1)):
    s1.append(s1[i] + c1[i])

s2 = [0]
for i in range(0, len(c2)):
    s2.append(s2[i] + c2[i])

q = int(input())
for i in range(q):
    l, r = (int(x) for x in input().split())
    
    print(s1[r]-s1[l-1], s2[r]-s2[l-1])




