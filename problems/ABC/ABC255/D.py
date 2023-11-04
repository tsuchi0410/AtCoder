import bisect
n, q = (int(x) for x in input().split())
a = list(map(int,input().split()))
x = [int(input()) for _ in range(q)]

a.sort()
s = [0]
for i in range(n):
    s.append(s[i] + a[i])

for i in range(q):
    idx = bisect.bisect_left(a, x[i])
    small = x[i] * idx - s[idx]
    
    idx = bisect.bisect_right(a, x[i])
    big = (s[-1] - s[idx]) - x[i] * (len(a) - idx)
    
    print(small+big)
    