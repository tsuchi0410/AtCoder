import itertools
N = int(input())
A = list(map(int,input().split()))

A = sorted(A)
L = [A[-1],A[-2],A[-3]]
L = list(itertools.permutations(L))

ans = 0
for i in range(len(L)):
    res = str(L[i][0])+str(L[i][1])+str(L[i][2])
    ans = max(int(res),ans)

print(ans)
