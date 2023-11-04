import bisect
MOD = 10**9 + 7
S = input()
dic = {}
dic["A"] = []
dic["B"] = []
dic["C"] = []
dic["?"] = []

for i in range(len(S)):
    dic[S[i]].append(i)

ans = 0

for v in dic["B"]:
    la = bisect.bisect_left(dic["A"], v)
    lq = bisect.bisect_left(dic["?"], v)
    a = la * (3 ** lq) + lq * (3 ** (lq - 1))
    rc = len(dic["C"]) - bisect.bisect_left(dic["C"], v)
    rq = len(dic["?"]) - bisect.bisect_left(dic["?"], v)
    c = rc * (3 ** rq) + rq * (3 ** (rq - 1))
    ans += a * c
    ans %= MOD

for v in dic["?"]:
    la = bisect.bisect_left(dic["A"], v)
    lq = bisect.bisect_left(dic["?"], v)
    a = la * (3 ** lq) + lq * (3 ** (lq - 1))
    rc = len(dic["C"]) - bisect.bisect_left(dic["C"], v)
    rq = len(dic["?"]) - bisect.bisect_right(dic["?"], v)
    c = rc * (3 ** rq) + rq * (3 ** (rq - 1))
    ans += a * c
    ans %= MOD

print(int(ans))
