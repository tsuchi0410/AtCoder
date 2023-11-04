def prime(N):
    if N==1:
        return list()
    A=list(range(2,N+1))
    p=list()
    while A[0]**2<=N:
        tmp=A[0]
        p.append(tmp)
        A=[e for e in A if e%tmp!=0]
    return p+A

n = int(input())
num = int(n**(1/3))
res = prime(num)
ans = 0 
for i in range(len(res)):
    for j in range(i+1,len(res)):
        if res[i] * res[j]**3 <= n:
            ans += 1
        else:
            break
print(ans)