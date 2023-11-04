vec = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
P = []
l = []
for i in range(12):
    l.append(list(input()))
    if len(l) == 4:
        P.append(l)
        l = []

for rotA in range(4):
    for rotB in range(4):
        for rotC in range(4):
            for v1 in range(4):
                for v2 in range(4):
                    for v3 in range(4):
                        for dy1, dx1 in vec:
                            fp1 = True
                            for ii in range(4):
                                for jj in range(4):
                                    if P[0][ii][jj] == "#":
                                        if not 0 <= ii + dy1 + v1 <= 3:
                                            fp1 = False
                                        if not 0 <= jj + dx1 + v1 <= 3:
                                            fp1 = False
                            if fp1 == False:
                                continue
                            for dy2, dx2 in vec:
                                fp2 = True
                                for ii in range(4):
                                    for jj in range(4):
                                        if P[1][ii][jj] == "#":
                                            if not 0 <= ii + dy2 + v2 <= 3:
                                                fp2 = False
                                            if not 0 <= jj + dx2 + v2 <= 3:
                                                fp2 = False
                                if fp2 == False:
                                    continue
                                for dy3, dx3 in vec:
                                    fp3 = True
                                    G = [[0] * 4 for _ in range(4)]
                                    for ii in range(4):
                                        for jj in range(4):  
                                            if P[2][ii][jj] == "#":
                                                if not 0 <= ii + dy3 + v3 <= 3:
                                                    fp3 = False
                                                if not 0 <= jj + dx3 + v3 <= 3:
                                                    fp3 = False
                                    if fp3 == False:
                                        continue

                                    if fp1 == fp2 == fp3 == True:
                                        for ii in range(4):
                                            for jj in range(4):
                                                if P[0][ii][jj] == "#":
                                                    G[ii + dy1 + v1][jj + dx1 + v1] += 1
                                                if P[1][ii][jj] == "#":
                                                    G[ii + dy2 + v2][jj + dx2 + v2] += 1
                                                if P[2][ii][jj] == "#":
                                                    G[ii + dy3 + v3][jj + dx3 + v3] += 1
                                        
                                        fans = True
                                        for i in range(4):
                                            for j in range(4):
                                                if G[i][j] != 1:
                                                    fans = False

                                        if fans == True:
                                            print("Yes")
                                            exit()

            P[2] = [list(row) for row in zip(*P[2][::-1])]
        P[1] = [list(row) for row in zip(*P[1][::-1])]
    P[0] = [list(row) for row in zip(*P[0][::-1])]

print("No")