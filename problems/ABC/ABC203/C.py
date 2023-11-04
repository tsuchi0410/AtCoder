N, K = (int(x) for x in input().split())

L = []
for i in range(N):
    a,b = (int(x) for x in input().split())
    L.append([a,b])

L = sorted(L, key=lambda x: x[0])

move = [0,K]
for i in range(N):
    # 移動判定
    if L[i][0]-move[0] <= move[1]:
        move[1] = move[1] - (L[i][0] - move[0])
        move[0] = L[i][0]
        move[1] += L[i][1]
    else:
        move[0] += move[1]
        print(move[0])
        exit()
    
    if i == N-1:
        move[0] += move[1]
        print(move[0])

    
