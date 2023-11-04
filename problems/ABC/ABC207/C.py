import copy

N = int(input())
L = []
for i in range(N):
    t, a, b = (int(x) for x in input().split())

    if t == 2:
        b -= 0.5
    elif t == 3:
        a += 0.5
    elif t == 4:
        a += 0.5
        b -= 0.5

    L.append([a,b])

ans = 0
for i in range(N):
    for j in range(N):
        if i >= j:
            continue
        
        if max(L[i][0], L[j][0]) <= min(L[i][1], L[j][1]):
            ans += 1

print(ans)






