X,Y,N = (int(x) for x in input().split())


cnt = 0
ans = 0
if 3*X >= Y:
    cnt = N // 3
    ans = cnt*Y
    ans += (N-cnt*3)*X
    print(ans)
    exit()
else:
    ans += N*X
    print(ans)
    exit()
