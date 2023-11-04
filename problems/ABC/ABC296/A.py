N = int(input())
S = input()

if S[0] == "M":
    f = True
else:
    f = False

for i in range(1, N):
    if S[i] == "M":
        ff = True
    else:
        ff = False
    
    if f == ff:
        print("No")
        exit()
    else:
        f = ff

print("Yes")