n = int(input())
a = list(map(int,input().split()))

stock = 0
a = list(set(a))
a = sorted(a)
stock = n - len(a)
for i in range(stock):
    a.append(10 ** 9 + (i+1))

ans = 0
cnt = 1
i = 0
while(1):
    if cnt == a[i]:
        cnt += 1
        i += 1
        ans += 1
    elif n >= 2:
        cnt += 1
        n -= 1
        ans += 1
    
    n -= 1
    if n == 0:
        print(ans)
        exit()
    
    
        