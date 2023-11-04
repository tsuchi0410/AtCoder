N, M = map(int, input().split())
S = [input() for _ in range(N)]
L = ["###.?????",
     "###.?????",
     "###.?????",
     "....?????",
     "?????????",
     "?????....",
     "?????.###",
     "?????.###",
     "?????.###"]

ans = []
for i in range(N - 8):
    for j in range(M - 8):
        f = True
        for k in range(9):
            for l in range(9):
                if L[k][l] == "#" and S[i + k][j + l] == ".":
                    f = False
                elif L[k][l] == "." and S[i + k][j + l] == "#":
                    f = False
        if f == True:
            ans.append([i + 1, j + 1])

ans.sort()
for i in ans:
    print(*i)
        
        