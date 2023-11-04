T = int(input())

for i in range(T):
    N = int(input())
    S = input()
    
    l = []
    for j in range(N):
        if S[j] == "1":
            l.append(j)
    
    if len(l) == 0:
        print(0)
    elif len(l) % 2 == 1:
        print(-1)
    else:
        if len(l) >= 4:
            print(len(l) // 2)
        elif l[1] - l[0] >= 2:
            print(1)
        
        # 隣接
        elif l[1] - l[0] == 1:
            if N == 3:
                print(-1)
            elif N == 4 and S == "0110":
                print(3)
            else:
                print(2)