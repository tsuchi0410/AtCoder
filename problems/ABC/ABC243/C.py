N = int(input())
L = []
for _ in range(N):
    X, Y = map(int, input().split())
    L.append([X, Y])
S = input()

dic_L = {}
dic_R = {}
for i in range(N):
    v = S[i]
    X = L[i][0]
    Y = L[i][1]
    if v == "R":
        if not Y in dic_R:
            dic_R[Y] = X
        else:
            dic_R[Y] = min(dic_R[Y], X)
        if Y in dic_L:
            if min(dic_R[Y], dic_L[Y]) == dic_R[Y]:
                print("Yes")
                exit()
    
    elif v == "L":
        if not Y in dic_L:
            dic_L[Y] = X
        else:
            dic_L[Y] = max(dic_L[Y], X)
        if Y in dic_R:
            if min(dic_R[Y], dic_L[Y]) == dic_R[Y]:
                print("Yes")
                exit()

print("No")