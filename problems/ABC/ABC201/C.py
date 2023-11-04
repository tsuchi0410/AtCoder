S = input()
st1 = set()
st2 = set()
for i in range(len(S)):
    if S[i] == "o":
        st1.add(str(i))
    elif S[i] == "?":
        st2.add(str(i))

ans = 0
for i in range(10000):
    num = str(i)
    num = num.zfill(4)
    st3 = set()
    for j in num:
        st3.add(j)

    if len(st1 & st3) == len(st1):
        st3 -= st1
        if len(st2 & st3) == len(st3):
            ans += 1
print(ans)