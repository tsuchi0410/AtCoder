S = input()
l = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(S)):
    if not S[i] in l:
        print(i + 1)
        
    