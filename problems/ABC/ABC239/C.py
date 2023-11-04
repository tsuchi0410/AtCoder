x1, y1, x2, y2 = map(int, input().split())
vec = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
ans = []
for i, j in vec:
    ans.append([x1 + i, y1 + j])
for i, j in vec:
    if [x2 + i, y2 + j] in ans:
        print("Yes")
        exit()
print("No")