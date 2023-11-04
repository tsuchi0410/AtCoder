from collections import defaultdict
def primes(n):
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
ans = 0

dic = defaultdict(int)
for i in range(2, N + 1):
    res = primes(i)
    for j in res:
        dic[j[0]] += j[1]   

# 75
for k, v in dic.items():
    if k != 1 and v >= 74:
        ans += 1

# 25 * 3
for k1, v1 in dic.items():
    for k2, v2 in dic.items():
        if k1 == 1:
            continue
        if k2 == 1:
            continue
        if k1 == k2:
            continue
        if v1 >= 24 and v2 >= 2:
            ans += 1

# 15 * 5
for k1, v1 in dic.items():
    for k2, v2 in dic.items():
        if k1 == 1:
            continue
        if k2 == 1:
            continue
        if k1 == k2:
            continue
        if v1 >= 14 and v2 >= 4:
            ans += 1

for k1, v1 in dic.items():
    for k2, v2 in dic.items():
        for k3, v3 in dic.items():
            if k1 == 1:
                continue
            if k2 == 1:
                continue
            if k3 == 1:
                continue
            if k1 == k2 or k1 == k3 or k2 == k3:
                continue
            if k1 < k2:
                continue
            if v1 >= 4 and v2 >= 4 and v3 >= 2:
                ans += 1

print(ans)