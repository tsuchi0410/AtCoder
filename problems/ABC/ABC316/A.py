S = input()
L = ["a", "e", "i", "o", "u"]
ans = []
for i in S:
    if not i in L:
        ans.append(i)
print("".join(ans))