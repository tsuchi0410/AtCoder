import bisect
n = int(input())
a = list(map(int,input().split()))
q = int(input())

a = sorted(a)
for i in range(q):
    b = int(input())
    idx = bisect.bisect_left(a, b)
    if idx == 0:
        print(abs(b - a[idx]))
    elif idx == len(a):
        print(abs(b - a[idx-1]))
    else:
        print(min(abs(b - a[idx-1]), abs(b - a[idx])))
