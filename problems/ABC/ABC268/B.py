S = input()
T = input()

S = list(S)
T = list(T)

if len(S) > len(T):
    print('No')
    exit()

for i in range(len(S)):
    if S[i] != T[i]:
        print('No')
        exit()

print('Yes')