from itertools import*

N, K = map(int, input().split())
S = list(input())
lst = [[k,len(list(v))] for k,v in groupby(S)]

l = 0
cnt = 0
ans = 0
for r in range(len(lst)):
    k = lst[r][0]
    v = lst[r][1]
    if k == "1":
        cnt += v
    elif k == "0":
        if K == 0:
            if lst[l][0] == "1":
                cnt -= lst[l][1]
                cnt -= lst[l + 1][1]
                l += 2
            else:
                cnt -= lst[l][1]
                l += 1
        else:
            K -= 1
        cnt += v
    ans = max(ans, cnt)
print(ans)