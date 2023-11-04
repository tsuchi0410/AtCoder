n = int(input())

if n == 0:
    print('1')
    exit()
    
ans = 0
for i in range(n+1):
    
    if i == 0:
        ans = 1
    else:
        ans = i * ans

print(ans)