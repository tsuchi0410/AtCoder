n = int(input())
l = list()

vector = [[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]

max_val = -1
for i in range(n):
    s = input()
    l.append(s)

print(l)

for i in range(n):
    for j in range(n):
        for direct in vector:
            x, y = i, j
            num = str()
            for k in range(n):
                x += direct[0]
                y += direct[1]
                num += l[x%n][y%n]
                print(num)
            num = int(num)
            max_val = max(max_val, num)
print(max_val)