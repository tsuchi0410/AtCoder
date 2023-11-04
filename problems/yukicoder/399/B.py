T = int(input())
for _ in range(T):
    y, x = map(int, input().split())
    cnt = 0
    for i in range(x, 61):
        if y >> i & 1 == 1:
            cnt = i
        else:
            break
    ans = 0
    for i in range(cnt + 1):
        ans += 1 << i
    print(ans)