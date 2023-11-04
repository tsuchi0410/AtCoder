# N! が素数 p で何回割れるかを求める
# ルジャンドル関数
def legendre(N, p):
    res = 0
    while N > 0:
        res += N // p
        N //= p
    return res
