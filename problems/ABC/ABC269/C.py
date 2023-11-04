import itertools
N = int(input())

a = format(N, 'b')
a = str(a)
l = []
for i in range(len(a)):
    if a[i] == '1':
        l.append(len(a) - i)

ans = []
for i in range(len(l)+1):
    c = list(itertools.combinations(l, i))
    
    for j in c:
        
        if not j:
            ans.append(['0'])
            continue
    
        p = ['0'] * (max(j))
        for k in j:
            p[k-1] = '1'
        
        p2 = list(reversed(p))
        ans.append(p2)

ans2 = []
for i in ans:
    x = ''.join(i)
    ans2.append(int(x, 2))

ans2 = sorted(ans2)
for i in ans2:
    print(i)