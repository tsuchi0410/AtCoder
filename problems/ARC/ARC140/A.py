from collections import defaultdict

def make_div(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

N, K = map(int, input().split())
S = input()
rp = make_div(N)
for num in rp:
    L = []
    i = 0
    while True:
        if i + num == N:
            L.append(S[i:])
            break
        else:
            L.append(S[i : i + num])
        i += num
    
    # print(L)

    cnt = 0
    for i in range(len(L[0])):
        dic = defaultdict(int)
        for j in range(len(L)):
            dic[ord(L[j][i])] += 1
        d = 0
        for k, v in dic.items():
            d = max(d, v)
        cnt += len(L) - d
    
    # print(dic)

    if cnt <= K:
        print(num)
        exit()

