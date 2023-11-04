G = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
A, B = map(int, input().split())
for i, e in enumerate(G):
    if A in e and B in e:
        if abs(G[i].index(A) - G[i].index(B)) == 1:
            print("Yes")
            exit()
print("No")