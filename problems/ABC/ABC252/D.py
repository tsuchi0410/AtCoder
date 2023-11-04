import bisect
n = int(input())
a = list(map(int,input().split()))

a.sort()
ans = 0
for l in range(n):
    
    j_idx1 = bisect.bisect_left(a, a[l])
    j_idx2 = bisect.bisect_right(a, a[l])
    
    i = j_idx1
    k = len(a) - j_idx2
    
    ans += i * k

print(ans)