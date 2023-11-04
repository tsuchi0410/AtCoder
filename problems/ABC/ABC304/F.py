# 約数列挙 √N
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


N = int(input())
S = input()
MOD = 998244353

div = make_div(N)
div.pop()
dic = {}
for i in div:
    st = set()
    for j in range(N):
        if S[j] == ".":
            st.add(j % i)
    L = [0] * N
    for j in range(N):
        if j % i in st:
            L[j] = 1
    cnt = 1
    for j in range(i):
        if L[j] == 0:
            cnt *= 2
            cnt %= MOD
    dic[i] = cnt

for k1, v1 in dic.items():
    for k2, v2 in dic.items():
        if k1 >= k2:
            continue
        if k2 % k1 == 0:
            dic[k2] -= dic[k1]

ans = 0
for v in dic.values():
    ans += v
    ans %= MOD
print(ans)
