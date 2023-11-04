H, W = map(int,input().split())
S = [input() for _ in range(H)]
vec = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
for i in range(H):
    for j in range(W):
        for y, x in vec:
            if not 0 <= i + y * 4 < H:
                continue
            if not 0 <= j + x * 4 < W:
                continue
            st = ""
            for k in range(5):
                st += S[i + y * k][j + x * k]
            if st == "snuke":
                for k in range(5):
                    print(i + y * k + 1, j + x * k + 1)
                exit()