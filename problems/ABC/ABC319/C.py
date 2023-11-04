import itertools

C = [0] * 3
for i in range(3):
    C[i] = list(map(int, input().split()))

check = set()
# 横
for i in range(3):
    for j in range(2):
        if C[i][j] == C[i][j + 1]:
            if j == 0:
                check.add((i, 2))
            else:
                check.add((i, 0))

# 縦
for j in range(3):
    for i in range(2):
        if C[i][j] == C[i + 1][j]:
            if i == 0:
                check.add((2, j))
            else:
                check.add((0, j))

# 斜め
if C[0][0] == C[1][1]:
    check.add((2, 2))


lst = list(itertools.permutations([1,2,3,4,5,6,7,8,9], 9))
cnt = 0
for i in lst:
    st = set(i)
    for num in i:
        if num == 1 or num == 2 or num == 3:
            if 