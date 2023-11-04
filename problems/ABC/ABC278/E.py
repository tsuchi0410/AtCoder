H, W, N, h, w = (int(x) for x in input().split())
a = []

for i in range(H):
    aa = list(map(int,input().split()))
    a.append(aa)

li = [0] * (N+1)
k = 0; l = 0
for i in range(H):
    for j in range(W):
        if k <= i < k+h and l <= j < l+w:
            pass
        else:
            li[a[i][j]] += 1

for i in range(H-(h-1)):
    l = []
    if i != 0:
        for k in range(w):
            li[a[i-1][k]] += 1
            li[a[i+h-1][k]] -= 1
        l.append(N - li.count(0) - 1)
        
    for j in range(W-(w)):
        if i == 0 and j == 0:
            continue
        
        for k in range(i+h):
            li[a[k][j+w]] += 1
            li[a[k][j-1]] -= 1
        l.append(N - li.count(0) - 1)
    print(l)
    




