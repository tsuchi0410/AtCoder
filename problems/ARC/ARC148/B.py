import copy
N = int(input())
S = input()

S = list(S)
for i in range(N):
    res = copy.copy(S)
    
    for j in range(i, N):
        
        l = i
        r = j+1
        
        b = res[l:r]
                