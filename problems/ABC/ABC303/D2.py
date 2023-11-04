from itertools import*
X, Y, Z = map(int,input().split())
S = input()
L = [[k,len(list(v))] for k,v in groupby(S)]
caps = False
ans = 0
for i in range(len(L)):
    rec = 0
    key = L[i][0]
    cnt = L[i][1]
    if key == "a":
        if caps == False:
            if X * cnt < Z + Y * cnt:
                rec = X * cnt
            else:
                rec = Z + Y * cnt
                caps = True
        elif caps == True:
            if Y * cnt < Z + X * cnt:
                rec = Y * cnt
            else:
                rec = Z + X * cnt
                caps = False
    elif key == "A":
        if caps == True:
            if X * cnt < Z + Y * cnt:
                rec = X * cnt
            else:
                rec = Z + Y * cnt
                caps = False
        elif caps == False:
            if Y * cnt < Z + X * cnt:
                rec = Y * cnt
            else:
                rec = Z + X * cnt
                caps = True
    ans += rec 
print(ans)       