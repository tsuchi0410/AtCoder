H = int(input())
ans = 0
cnt = 1
while True:
    if H == 1:
        ans += cnt
        print(ans)
        exit()
    ans += cnt
    H //= 2
    cnt *= 2