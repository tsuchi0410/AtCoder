N,M = (int(x) for x in input().split())
B = []
for i in range(N):
    B.append(list(map(int,input().split())))

l = []
loc = []
buf = 0
for i in range(N):
    for j in range(M):
        buf = (B[i][j]-1) % 7
        l.append(buf)
    loc.append(l)
    l = []
    
#print(loc)
for i in range(0, N):
    for j in range(0, M):

        if j >= 1:
            if loc[i][j] - loc[i][j-1] != 1:
                print("No")
                exit()

            if B[i][j] - B[i][j-1] != 1:
                print("No")
                exit()
        
        if i >= 1:
            if loc[i][j] != loc[i-1][j]:
                print("No")
                exit()

            if B[i][j] - B[i-1][j] != 7:
                print("No")
                exit()
            

print("Yes")        

        