N, Q = map(int, input().split())
l = list(range(N))
pos = list(range(N))
for _ in range(Q):
    x = int(input())
    x -= 1
    idx = pos[x]
    if idx < N - 1:
        l[idx], l[idx + 1] = l[idx + 1], l[idx]
        pos[l[idx]], pos[l[idx + 1]] = pos[l[idx + 1]], pos[l[idx]]
    else:
        l[idx - 1], l[idx] = l[idx], l[idx - 1]
        pos[l[idx - 1]], pos[l[idx]] = pos[l[idx]], pos[l[idx - 1]]
    
for i in range(N):
    print(l[i] + 1, end = " ")