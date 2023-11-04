N = int(input())

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

res = prime(N)
#print(res)
ans = 0
for i in range(len(res)):
    num = res[i][1]
    cnt = 0
    while True:
        cnt += 1
        num -= cnt
        if num == 0:
            break
        elif num < 0:
            cnt -= 1
            break
    ans += cnt

print(0) if N == 1 else print(ans)