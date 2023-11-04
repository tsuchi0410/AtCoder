N, M, H, K = map(int,input().split())
S = input()
st = set()
for i in range(M):
    x, y = map(int,input().split())
    st.add((y, x))

h = 0
w = 0
for i in range(len(S)):
    if S[i] == "R":
        w += 1
    if S[i] == "L":
        w -= 1
    if S[i] == "U":
        h += 1
    if S[i] == "D":
        h -= 1
    
    H -= 1
    if H < 0:
        print("No")
        exit()

    if (h, w) in st:
        if H < K:
            H = K
            st.remove((h, w))


print("Yes")