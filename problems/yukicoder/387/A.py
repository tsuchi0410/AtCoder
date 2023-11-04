N = int(input())
P = list(map(int,input().split()))
ans = 0
while True:
    f = False
    for i in range(N):
        if P[i] != i + 1:
            f = True
            ans += 1
            for j in range(N):
                if P[j] == i + 1:
                    P[i], P[j] = P[j], P[i]
            break
    if f == True:
        continue
    else:
        break
print(ans)