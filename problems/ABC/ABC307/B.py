N = int(input())
S = [input() for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        s = S[i] + S[j]
        f = True
        for k in range(len(s)):
            if s[k] != s[len(s) - 1 - k]:
                f = False
        
        if f == True:
            print("Yes")
            exit()
print("No")