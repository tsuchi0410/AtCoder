N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int,input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

L = []
st = set()
for i in range(N):
    if len(G[i]) >= 3:
        L.append(len(G[i]))
        for e in G[i]:
            st.add(e)
        st.add(i)

others = N - len(st)
if others != 0:
    for i in range(others // 3):
        L.append(2)

L.sort()
print(*L)
