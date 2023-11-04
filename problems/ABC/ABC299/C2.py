from itertools import*
N = int(input())
s = input()
l = [[k,len(list(v))] for k,v in groupby(s)]
# l = [len(list(v)) for k,v in groupby(s)]

if len(l) == 1:
    print("-1")
else:
    ans = 0
    for i in range(len(l)):
        if l[i][0] == "o":
            ans = max(ans, l[i][1])
    print(ans)