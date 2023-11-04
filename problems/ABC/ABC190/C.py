import copy
N,M = (int(x) for x in input().split())
A = []
B = []
for i in range(M):
    a,b = (int(x) for x in input().split())
    A.append(a)
    B.append(b)
K = int(input())
C = []
D = []
for i in range(K):
    c,d = (int(x) for x in input().split())
    C.append(c)
    D.append(d)
    
ans = 0
for i in range(1 << K):
    l = []
    cnt = 0
    AA = copy.copy(A)
    BB = copy.copy(B)
    for j in range(K):
        if (i >> j) & 1 == 1:
            l.append(C[j])
        else:
            l.append(D[j])
    
    for i in range(len(l)):
        for j in range(M):
            if AA[j] == l[i]:
                AA[j] = False    
            if BB[j] == l[i]:
                BB[j] = False
                
    for i in range(M):
        if AA[i] == False and BB[i] == False:
            cnt += 1
    
    ans = max(ans, cnt)


print(ans)