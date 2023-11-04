T = int(input())
for i in range(T):
    x1, x2, x3 = map(int, input().split())

    if x1 % 2 == x2 % 2 == x3 % 2 and (x1+x2+x3) % 3 == 0:
        ave = (x1+x2+x3) // 3
        ans = (abs(x1-ave) + abs(x2-ave) + abs(x3-ave)) // 4
        print(ans)
    else:
        print(-1)