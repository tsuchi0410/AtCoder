N = int(input())
L = []
for i in range(N):
    T, D = map(int, input().split())
    L.append([T, T + D])

L.sort(key=lambda x: x[1])

print(L)

x = L[0][0]
ans = 1
for i in range(N - 1):
    if L[i + 1][0] > x:
        x = L[i + 1][0]
        ans += 1
    elif L[i + 1][0] == x:
        if L[i + 1][1] > x:
            x += 1
            ans += 1
    else:
        if(L[i + 1][1] > x):
            x += 1
            ans += 1
    
    print("ans=", ans)
    print("i=", i)
    print("x=",x)

print(ans)


# // 1 2
# // 1 2
# // 2 3
# // 1 3
# // 1 5