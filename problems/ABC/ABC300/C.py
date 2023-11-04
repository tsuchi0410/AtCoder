H,W= map(int,input().split())
C = []
for i in range(H):
    c = input()
    C.append(c)

ans = [0] * (min(H, W) + 1)
for i in range(H):
    for j in range(W):
        if C[i][j] == "#":
            if i+1 >= H or j + 1 >= W:
                continue
            if i-1 < 0 or j-1 < 0:
                continue
            if C[i+1][j+1] == "#" and C[i+1][j-1] == "#" and C[i-1][j+1] == "#" and C[i-1][j-1] == "#":
                cnt = 0
                ii = i
                jj = j
                while True:
                    if ii+1 >= H or jj + 1 >= W:
                        break
                    if C[ii+1][jj+1] == "#":
                        cnt += 1
                        ii += 1
                        jj += 1
                    else:
                        break
                ans[cnt] += 1
print(*ans[1:])