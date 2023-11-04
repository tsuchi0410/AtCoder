import itertools
n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))

nl = list(range(n+1))
nl = nl[1:]
l = list(itertools.permutations(nl))

a = 0
b = 0
c = 0
for i in l:
    if list(i) == p:
        a = c
    if list(i) == q:
        b = c
    c += 1
    
print(abs(a-b))