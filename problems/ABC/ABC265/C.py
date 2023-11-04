H, W = (int(x) for x in input().split())
G = []
G2 = []
for i in range(H):
    s = input()
    G.append(s)
    G2.append([0] * len(s))


H -= 1
W -= 1
i = 0
j = 0


while(1):
    
    # U
    if G[i][j] == 'U' and i != 0:
        i -= 1
    # D
    elif G[i][j] == 'D' and i != H:
        i += 1
    # L
    elif G[i][j] == 'L' and j != 0:
        j -= 1
    # R
    elif G[i][j] == 'R' and j != W:
        j += 1
    
    # 成功
    else:
        print(i+1,j+1)
        exit()
    
    if G2[i][j] == 1:
        print("-1")
        exit()
    else:
        G2[i][j] = 1

    

    
    




