S = input()
B = []
for i in range(len(S)):
    if S[i] == "B":
        B.append((i+1) % 2)

B = set(B)
if len(B) == 1:
    print("No")
    exit()


for i in range(len(S)):
    if S[i] == "R":
        for j in range(i, len(S)):
            if S[j] == "K":
                for k in range(j, len(S)):
                    if S[k] == "R":
                        print("Yes")
                        exit()
print("No")