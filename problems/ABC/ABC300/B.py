H,W = map(int,input().split())
A = []
for i in range(H):
    a = input()
    A.append(a)
B = []
for i in range(H):
    b = input()
    B.append(b)


for s in range(H):
    for t in range(W):
        f = True
        for i in range(H):
            for j in range(W):
                if B[i][j] == A[i-s][j-t]:
                    pass
                else:
                    f = False
    
        if f == True:
            print("Yes")
            exit()

print("No")