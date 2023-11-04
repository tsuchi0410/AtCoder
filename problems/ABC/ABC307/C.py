HA, WA = map(int, input().split())
A = [input() for _ in range(HA)]
HB, WB = map(int, input().split())
B = [input() for _ in range(HB)]
HX, WX = map(int, input().split())
X = [input() for _ in range(HX)]

sa = set()
for i in range(HA):
    for j in range(WA):
        if A[i][j] == "#":
            sa.add((i, j))

sb = set()
for i in range(HB):
    for j in range(WB):
        if B[i][j] == "#":
            sb.add((i, j))


sx = set()
for i in range(HX):
    for j in range(WX):
        if X[i][j] == "#":
            sx.add((i, j))

for ia in range(-10, 11, 1):
    for ja in range(-10, 11, 1):
        for ib in range(-10, 11, 1):
            for jb in range(-10, 11, 1):
                sa2 = set()
                sb2 = set()
                for y, x in sa:
                    sa2.add((y + ia, x + ja))
                for y, x in sb:
                    sb2.add((y + ib, x + jb))
                s = sa2 | sb2
                if s == sx:
                    print("Yes")
                    exit()

print("No")