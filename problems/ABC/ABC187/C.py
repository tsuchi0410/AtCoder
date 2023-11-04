N = int(input())
st = set()
for _ in range(N):
    S = input()
    if S[0] == "!":
        ss = S[1:]
        if ss in st:
            print(ss)
            exit()
        else:
            st.add(S)
    else:
        ss = "!" + S
        if ss in st:
            print(S)
            exit()
        else:
            st.add(S)

print("satisfiable")