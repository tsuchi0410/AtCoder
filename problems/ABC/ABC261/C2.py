N = int(input())

dic = {}
for i in range(N):
    S = str(input())

    if S in dic:
        dic[S] += 1
        print(S+"("+str(dic[S])+")")
    else:
        dic[S] = 0
        print(S)
