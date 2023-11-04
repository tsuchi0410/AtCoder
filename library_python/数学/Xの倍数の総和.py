# Xの倍数の総和
# （初項＋末項）＊項数 / 2
def baisu_souwa(X, a):
    syokou = a
    kou = X // a
    makkou = kou * a
    ans = (syokou + makkou) * kou // 2
    return ans
