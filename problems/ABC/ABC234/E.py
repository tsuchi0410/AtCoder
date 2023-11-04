import bisect

X = int(input())
L = []
for sa in range(-9, 10, 1):  # 等差
    for start in range(1, 10, 1):  # 最初の値
        num = start
        res = ""
        while True:
            if num < 0 or num > 9:
                break
            if len(str(res)) >= 18:
                break
            res += str(num)
            num += sa
            L.append(int(res))
L.sort()
res = bisect.bisect_left(L, X)
print(L[res])