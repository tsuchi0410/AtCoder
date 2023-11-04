import itertools
N, M = map(int, input().split())
G1 = [set() for _ in range(N)]
dic = {}
for i in range(N):
    dic[i] = i
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G1[A].add(B)
    G1[B].add(A)
q = []
for i in range(M):
    C, D = map(int, input().split())
    C -= 1
    D -= 1
    q.append([C, D])

lst = list(itertools.permutations(list(range(N)), N))
for balls in lst:
    G2 = [set() for _ in range(N)]
    i = 0
    for k, v in dic.items():
        dic[k] = balls[i]
        i += 1 
    for u, v in q:
        G2[dic[u]].add(dic[v])
        G2[dic[v]].add(dic[u])
    if G1 == G2:
        print("Yes")
        exit()
print("No")