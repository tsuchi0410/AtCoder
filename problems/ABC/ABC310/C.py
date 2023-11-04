N = int(input())
st = set()
for _ in range(N):
    S = input()
    if S in st or S[::-1] in st:
        continue
    else:
        st.add(S)
    
print(len(st))