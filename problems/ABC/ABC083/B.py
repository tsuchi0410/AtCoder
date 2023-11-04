L = list(map(int,input().split()))

cnt = 0
ans = 0
for i in range(L[0] + 1):
    a = i
    while a > 0:
        cnt += a % 10
        a = a // 10

    if cnt >= L[1] and L[2] >= cnt:    
        ans += i

    cnt = 0

print(ans)
