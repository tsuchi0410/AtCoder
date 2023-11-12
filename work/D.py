S = input()
L = []
for i in range(len(S)):
    L.append(S[i])
    if L[-3:] == ["A", "B", "C"]:
        for j in range(3):
            L.pop()

print("".join(L))