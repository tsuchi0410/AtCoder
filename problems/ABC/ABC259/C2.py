S = str(input())
T = str(input())

S1 = []
T1 = []
c = 0
buf = str()

for i in range(len(S)):
    if i == len(S)-1:
        if c == 0:
            S1.append(S[i])
        else:
            for j in range(c+1):
                buf += S[i]
            S1.append(buf)
        c = 0
        buf = str()
        break

    if S[i] == S[i+1]:
        c += 1
    else:
        if c == 0:
            S1.append(S[i])
        else:
            for j in range(c+1):
                buf += S[i]
            S1.append(buf)
        c = 0
        buf = str()

for i in range(len(T)):
    if i == len(T)-1:
        if c == 0:
            T1.append(T[i])
        else:
            for j in range(c+1):
                buf += T[i]
            T1.append(buf)
        break

    if T[i] == T[i+1]:
        c += 1
    else:
        if c == 0:
            T1.append(T[i])
        else:
            for j in range(c+1):
                buf += T[i]
            T1.append(buf)
        c = 0
        buf = str()

f = 1
for i in range(len(S1)):
    if len(S1[i]) > len(T1[i]):
        f = 0
        break
    else:
        if len(S1[i]) == 1 and len(T1[i]) >= 2:
            f = 0
            break
    if len(S1) != len(T1):
        f = 0
        break

    if not S1[i][0] == T1[i][0]:
        f = 0
        break
    
if f == 1:
    print("Yes")
else:
    print("No")

                


