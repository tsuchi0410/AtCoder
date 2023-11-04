H, W = map(int,input().split())
N = int(input())
l = list(map(int,input().split()))
a = {}
for i in range(N):
    a[i + 1] = l[i]
G = [[0] * W for _ in range(H)]
c = 1
i = 0
j = 0
f = False
cnt = 0
while True:
    G[i][j] = c
    a[c] -= 1
    if f == False:
        j += 1
    else:
        j -= 1
    cnt += 1
    if j == -1:
        f = False
        j += 1
        i += 1
    if j == W:
        f = True
        j -= 1
        i += 1
    
    if a[c] == 0:
        c += 1
    if cnt == H * W:
        break

for k in G:
    print(*k)