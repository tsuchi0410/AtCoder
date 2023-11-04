N, K = map(int, input().split())
a = list(map(int, input().split()))
all = K // N
K %= N

b = sorted(a)
s = set()
for i in range(K):
    s.add(b[i])

for i in range(N):
    if a[i] in s:
        print(all + 1)
    else:
        print(all)