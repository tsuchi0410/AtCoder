from itertools import*
S = input()
if S == S[::-1]:
    print("Yes")
else:
    L = [[k,len(list(v))] for k,v in groupby(S)]
    if L[-1][0] != "a":
        print("No")
    else:
        if L[0][0] == "a":
            if L[0][1] <= L[-1][1]:
                L[0][1] = L[-1][1]
            else:
                print("No")
                exit()
        else:
            L = [["a", L[-1][1]]] + L
        
        if L == L[::-1]:
            print("Yes")
        else:
            print("No")
