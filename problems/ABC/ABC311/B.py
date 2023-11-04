N, D = map(int, input().split())

L = []
for i in range(N):
    S = input()
    L.append(S)

ans = 0
cnt = 0
for col in zip(*L):
    f = True
    for i in col:
        if i == "x":
            f = False
    
    if f == True:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0

print(ans)