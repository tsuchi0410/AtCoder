import sys
S = str(input())

dic = {}
for i in S:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
    

for i in dic:
    if dic[i] == 1:
        print(i)
        sys.exit()

print("-1")