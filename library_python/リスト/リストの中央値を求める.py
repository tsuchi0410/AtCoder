def median(lst):
    """
    リストの中央値を返す
    """
    n = len(lst)
    s = sorted(lst)
    # リストの要素数が奇数の場合
    if n % 2 == 1:
        return s[n//2]
    # リストの要素数が偶数の場合
    else:
        return (s[n//2-1] + s[n//2])/2