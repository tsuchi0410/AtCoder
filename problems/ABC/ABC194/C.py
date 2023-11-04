from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))

d = defaultdict(int)
for i in range(n):
    a[i] += 200
    d[a[i]] += 1

ans = 0
for i in d:
    for j in d:
        ans += abs(i-j)**2 * (d[i]*d[j])

print(ans//2)