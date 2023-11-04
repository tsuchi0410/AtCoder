import math
n,m=(int(x) for x in input().split())
a=list(map(int,input().split()))

# 素因数分解
def f(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

s = set()
for i in range(n):
    r = f(a[i])
    for j in r:
        s.add(j[0])

l = [False] * (m+1)
for i in s:
    if i == 1:
        continue
    for j in range(i, m+1, i):
        l[j] = True

ans = []
for i in range(1, m+1):
    if l[i] == False:
        ans.append(i)

print(len(ans))
print(*ans,sep='\n')