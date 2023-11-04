s = input()
t = input()

r = [True]
for i in range(len(t)):
    if r[i] == True:
        if s[i] == t[i] or s[i] == "?" or t[i] == "?":
            r.append(True)
            continue
    r.append(False)

s = s[::-1]
t = t[::-1]
l = [True]
for i in range(len(t)):
    if l[i] == True:
        if s[i] == t[i] or s[i] == "?" or t[i] == "?":
            l.append(True)
            continue
    l.append(False)

l.reverse()
for i in range(len(r)):
    if r[i] == True and l[i] == True:
        print("Yes")
    else:
        print("No")
