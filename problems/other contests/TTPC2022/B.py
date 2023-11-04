import itertools
n,x = (int(x) for x in input().split())
a = list(map(int,input().split()))

inf = 1000
dp = [[0] * inf for _ in range(n)]

for i in range(n):
    for j in range(inf):
        
        l = list(itertools.permutations(str(x)))
        for k in l:
            num = int(''.join(k))
            if num - a[i]>= 0:
                dp[i][num-a[i]] += 1
        
        if dp[i][j] > 0:
            next_x = j - x
            if next_x >= 0:
                l = list(itertools.permutations(str(next_x)))
            for k in l:
                num = int(''.join(k))
                if num - a[i]>= 0:
                    dp[i][num-a[i]] += 1