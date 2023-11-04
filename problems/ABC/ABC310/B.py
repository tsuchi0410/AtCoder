N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]

T = []
for i in range(N):
    P = L[i][0]
    S = set()
    for j in range(L[i][1]):
        S.add(L[i][j + 2])
    T.append([P, S])

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        
        Pi = T[i][0]
        Pj = T[j][0]


        if Pi > Pj:
            S = T[j][1] & T[i][1]
            if len(S) == len(T[i][1]):
                print("Yes")
                exit()
        
        if Pi == Pj:
            S = T[j][1] & T[i][1]
            if len(S) == len(T[i][1]):
                if len(T[j][1]) > len(S):
                    print("Yes")
                    exit()

print("No")
