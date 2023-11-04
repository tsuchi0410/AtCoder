H,W=map(int,input().split())
S=[input() for _ in range(H)]
vec=[[0,1],[0,-1],[1,0],[-1,0]]
for i in range(H):
    for j in range(W):
        if S[i][j]==".":
            cnt = 0
            for y,x in vec:
                if not 0 <= i + y < H:
                    continue
                if not 0 <= j + x < W:
                    continue
                if S[i+y][j+x] == "#":
                    cnt += 1
            if cnt >= 2:
                print(i+1,j+1)
                exit()