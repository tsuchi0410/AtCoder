N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

S_grid = []
cnt_S = 0
for i in range(N):
    for j in range(N):
        if S[i][j] == "#":
            S_grid.append([i, j])
            cnt_S += 1

cnt_T = 0
for i in range(N):
    for j in range(N):
        if T[i][j] == "#":
            cnt_T += 1

if cnt_T != cnt_S:
    print("No")
else:
    for _ in range(4):
        for y in range(-N, N):
            for x in range(-N, N):
                f = True
                for si, sj in S_grid:
                    if not (0 <= y+si < N and 0 <= x+sj < N and T[y+si][x+sj] == "#"):
                        f = False
                        break
                if f == True:
                    print("Yes")
                    exit()
        S_grid = [[y, N-1-x] for x, y in S_grid]
    print("No")