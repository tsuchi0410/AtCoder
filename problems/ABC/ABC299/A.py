N = int(input())
S = input()
for i in range(N):
    if S[i] == "|":
        for j in range(i+1, N):
            if S[j] == "*":
                for k in range(j+1, N):
                    if S[k] == "|":
                        print("in")
                        exit()

print("out")