M = int(input())
S1 = input()
S2 = input()
S3 = input()

st1 = set()
for i in range(M):
    st1.add(S1[i])

st2 = set()
for i in range(M):
    st2.add(S2[i])

st3 = set()
for i in range(M):
    st3.add(S3[i])

check = st1 & st2 & st3
if len(check) == 0:
    print(-1)
    exit()

ans = 10**18
N = 310
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j or j == k or k == i:
                continue
            n1 = S1[i % M]
            n2 = S2[j % M]
            n3 = S3[k % M]
            if n1 == n2 == n3:
                ans = min(ans, max(i, j, k))

print(ans)