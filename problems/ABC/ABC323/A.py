S = "x" + input()
for i in range(len(S)):
    if i >= 2:
        if i % 2 == 0:
            if S[i] == "1":
                print("No")
                exit()

print("Yes")