N = int(input())
S = input()
f1 = False
f2 = False
f3 = False
for i in range(N):
    if S[i] == "A":
        f1 = True
    elif S[i] == "B":
        f2 = True
    else:
        f3 = True
    
    if f1 == True and f2 == True and f3 == True:
        print(i + 1)
        exit()