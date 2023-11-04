L = list(map(int,input().split()))

d = {}
for i in L:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for i in d.values():
    if i != 2 and i != 3:
        print("No")
        exit()
        

print("Yes")