R, C = map(int, input().split())
B = []
for i in range(R):
    b = input()
    b = list(b)
    B.append(b)

for i in range(R):
    for j in range(C):
        if B[i][j] == ".":
            pass
        elif B[i][j] == "#":
            pass
        else:
            num = B[i][j]
            for ii in range(R):
                for jj in range(C):
                    if abs(i - ii) + abs(j - jj) <= int(num):
                        if B[ii][jj] == ".":
                            pass
                        elif B[ii][jj] == "#":
                            B[ii][jj] = "."
                        else:
                            pass
            B[i][j] = "."

for i in B:
    print(*i, sep = "")