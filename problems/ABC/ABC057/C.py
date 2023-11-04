def prime(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i==0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr

N = int(input())
res = prime(N)
lst = []
for k, v in res:
    for i in range(v):
        lst.append(k)
NUM = len(lst)
ans = 10**18
for i in range(2 ** NUM):
    l = [i >> j & 1 for j in range(NUM)]
    a = 1
    b = 1
    for j in range(len(l)):
        if l[j] == 0:
            a *= lst[j]
        else:
            b *= lst[j]
    ans = min(ans, max(len(str(a)), len(str(b))))
print(ans)