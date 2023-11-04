from collections import defaultdict
k = int(input())

def f(n):
    arr = defaultdict(int)
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr[i] = cnt
    if temp!=1:
        arr[temp] = 1
    if arr==[]:
        arr[n] = 1
    return arr

# 二分探索
def nibutan(d):
    
    l = 0
    r = 10**12 + 1
    
    while(1 < r - l):
        frag = 1
        center = (r + l) // 2
        for i in d:
            cnt = 0
            p = center
            while p > 0:
                cnt += p // i
                p //= i
            if cnt < d[i]:
                frag = 0
        
        if frag == 1:
            r = center
        else:
            l = center

    return l, r

d = f(k)
res = nibutan(d)
print(res[1])