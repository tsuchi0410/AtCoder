from itertools import permutations
S,K = input().split()
K = int(K)

st = set()
for it in permutations(S):
    st.add("".join(it))
st = sorted(st)

l = list(st)
print(l[K-1])