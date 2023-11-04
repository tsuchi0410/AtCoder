N, A, B = (int(x) for x in input().split())

G = [[] for i in range(N)]
for i in range(N):
    S = input()
    
    for j in range(len(S)):
        if S[j] == 'o':
            G[j].append(i)

# print(G)

if B in G[A]:
    print('Yes')
else:
    print('No')