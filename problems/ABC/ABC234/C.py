K = int(input())
S = bin(K)[2:]
L = []
for i in range(len(S)):
    if S[i] == "1":
        L.append("2")
    else:
        L.append("0")
print("".join(L))