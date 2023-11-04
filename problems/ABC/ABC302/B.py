H, W = map(int,input().split())
G = [input() for _ in range(H)]
for i in range(H):
    for j in range(W-4):
        if G[i][j] == "s" and G[i][j+1] == "n" and G[i][j+2] == "u" and G[i][j+3] == "k" and G[i][j+4] == "e":
            for k in range(5):
                print(i+1, j+1+k)
            exit()
        elif G[i][j] == "e" and G[i][j+1] == "k" and G[i][j+2] == "u" and G[i][j+3] == "n" and G[i][j+4] == "s":
            for k in range(4, -1, -1):
                print(i+1, j+1+k)
            exit()

for i in range(H-4):
    for j in range(W):
        if G[i][j] == "s" and G[i+1][j] == "n" and G[i+2][j] == "u" and G[i+3][j] == "k" and G[i+4][j] == "e":
            for k in range(5):
                print(i+1+k, j+1)
            exit()
        elif G[i][j] == "e" and G[i+1][j] == "k" and G[i+2][j] == "u" and G[i+3][j] == "n" and G[i+4][j] == "s":
            for k in range(4, -1, -1):
                print(i+1+k, j+1)
            exit()

for i in range(H-4):
    for j in range(W-4):
        if G[i][j] == "s" and G[i+1][j+1] == "n" and G[i+2][j+2] == "u" and G[i+3][j+3] == "k" and G[i+4][j+4] == "e":
            for k in range(5):
                print(i+1+k, j+1+k)
            exit()
        elif G[i][j] == "e" and G[i+1][j+1] == "k" and G[i+2][j+2] == "u" and G[i+3][j+3] == "n" and G[i+4][j+4] == "s":
            for k in range(4, -1, -1):
                print(i+1+k, j+1+k)
            exit()

for i in range(H-4):
    for j in range(4, W):
        if G[i][j] == "s" and G[i+1][j-1] == "n" and G[i+2][j-2] == "u" and G[i+3][j-3] == "k" and G[i+4][j-4] == "e":
            x = []
            for k in range(5):
                x.append(i+1+k)
            y = []
            for k in range(5):
                y.append(j+1-k)
            for k in range(5):
                print(x[k], y[k])
            exit()
        elif G[i][j] == "e" and G[i+1][j-1] == "k" and G[i+2][j-2] == "u" and G[i+3][j-3] == "n" and G[i+4][j-4] == "s":
            x = []
            for k in range(4,-1,-1):
                x.append(i+1+k)
            y = []
            for k in range(4,-1,-1):
                y.append(j+1-k)
            for k in range(5):
                print(x[k], y[k])
            exit()