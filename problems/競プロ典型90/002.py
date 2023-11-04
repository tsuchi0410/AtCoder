n = int(input())

if n % 2 != 0:
    print('')
    exit()

else:
    
    l = []
    for i in range(1 << n):
        
        l2 = []
        c = 0
        for j in range(n):
            if (i >> j) & 1 == 1:
                l2.append(1)
                c += 1
            else:
                l2.append(-1)
                c -= 1
        
        if c == 0:
            l.append(l2)
            

ans = []        
for i in l:
    
    cnt = 0
    f = 1
    for j in range(len(i)):
        cnt += i[j]
        
        if cnt < 0:
            f = 0
            break
    
    if f == 1:
        ans.append(i)

ans.sort(reverse = True)
for i in range(len(ans)):
    s = []
    for j in range(n):
        
        if ans[i][j] == 1:
            s.append('(')
        else:
            s.append(')')
    
    print(*s, sep = '')