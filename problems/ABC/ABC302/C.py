import itertools
N, M = map(int,input().split())
S = [input() for _ in range(N)]
lst = list(itertools.permutations(list(range(N))))


for i in lst:
    l = []
    for j in i:
        l.append(S[j])
    
    f = True
    for j in range(N-1):
        miss = 0
        for k in range(M):
            if l[j][k] != l[j+1][k]:
                miss += 1
        if miss != 1:
            f = False
            break
    
    if f == True:
        print("Yes")
        exit()

print("No")