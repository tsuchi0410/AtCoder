import itertools
N = int(input())

l = list(itertools.permutations(str(N)))

# print(l)

ans = -1
for i in range(len(l)):
    for j in range(1,len(l[i])):
        n1 = int(''.join(l[i][:j]))
        n2 = int(''.join(l[i][j:]))
        # print(n1,n2)

        ans = max(ans, n1*n2)

print(ans)        
        


