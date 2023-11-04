from collections import Counter
S = input()
T = input()

l = ["a", "t", "c", "o", "d", "e", "r", "@"]

CS = Counter(S)
CT = Counter(T)
atS = S.count("@")
atT = T.count("@")

dic = CS - CT

for k, v in dic.items():
    if k == "@":
        continue
    if not k in l:
        print("No")
        exit()
    atT -= v
    if atT < 0:
        print("No")
        exit()

dic = CT - CS
for k, v in dic.items():
    if k == "@":
        continue
    if not k in l:
        print("No")
        exit()
    atS -= v
    if atS < 0:
        print("No")
        exit()

print("Yes")