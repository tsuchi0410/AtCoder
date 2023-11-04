n = int(input())
a = list(map(int,input().split()))

l = []
ans = 0
for i in range(n):
    # append
    if len(l) == 0:
        l.append([a[i], 1])
    else:
        if l[-1][0] == a[i]:
            l[-1][1] += 1
        else:
            l.append([a[i], 1])
    ans += 1
    
    # delete
    if l[-1][0] <= l[-1][1]:
        num = l[-1][1] // l[-1][0]
        ans -= num * l[-1][0]
        l[-1][1] %= l[-1][0]
    
    if l[-1][1] == 0:
        del l[-1]
    
    print(ans)
