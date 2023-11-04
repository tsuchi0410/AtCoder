HA, WA = map(int, input().split())
A = [input() for _ in range(HA)]
HB, WB = map(int, input().split())
B = [input() for _ in range(HB)]
HX, WX = map(int, input().split())
X = [input() for _ in range(HX)]

vec = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]]

la = list()
for i in range(HA):
    for j in range(WA):
        if A[i][j] == "#":
            la.add((i, j))

lb = set()
for i in range(HB):
    for j in range(WB):
        if B[i][j] == "#":
            lb.add((i, j))


lx = []
for i in range(HX):
    for j in range(WX):
        if X[i][j] == "#":
            lx.append([i, j])

for y, x in vec:
    for c in range(22):
        f = True
        for i, j in lx:
            if not ((i + (y * c), j + (x * c)) in la or (i + (y * c), j + (x * c)) in lb):
                f = False
        if f == True:
            print("Yes")
            exit()

print("No")