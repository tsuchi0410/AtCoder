import itertools
A = list(map(int,input().split()))

l = list(itertools.permutations(A))
for i in l:
    if i[2]-i[1] == i[1]-i[0]:
         print("Yes")
         exit()

print("No")
