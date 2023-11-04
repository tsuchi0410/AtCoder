n = int(input())
h = list(map(int,input().split()))

idx = 0
m = -1
for i in range(n):
    if h[i] > m:
        m = h[i]
        idx = i + 1

print(idx)