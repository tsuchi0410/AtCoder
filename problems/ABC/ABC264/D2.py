S = str(input())

P = "atcoder"
N = len(P)
L = [P.index(x) for x in S]


# print(L)
cnt = 0
while(1):
    f = 0
    for i in range(N-1):
        if L[i+1] < L[i]:
            L[i],L[i+1] = L[i+1],L[i]
            cnt += 1
            f = 1
            # print(L)
    if f == 0:
        print(cnt)
        exit()

    