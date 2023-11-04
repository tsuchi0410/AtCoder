from collections import defaultdict

N = int(input())
p = list(map(int,input().split()))

l = []
for i in range(N):
    l.append((p[i]-i) % N)

l2 = [0] * N
for i in range(N):
    l2[(l[i]-1)%N] += 1
    l2[l[i]] += 1
    l2[(l[i]+1)%N] += 1


print(max(l2))