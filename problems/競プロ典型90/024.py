n, k = (int(x) for x in input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

sa = 0
for i in range(n):
    sa += abs(a[i] - b[i])
    

if k < sa:
    print('No')
else:
    if (k - sa) % 2 == 0:
        print('Yes')
    else:
        print('No')