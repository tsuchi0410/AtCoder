n = int(input())
s = input()
l = []
i = 0
while i < n:
    if s[i] == "n" and i + 1 < n:
        if s[i+1] == "a":
            l.append("nya")
            i += 1
        else:
            l.append(s[i])
    else:
        l.append(s[i])
    i += 1

print("".join(l))