N = int(input())
X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

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

rx = median(X)
ry = median(Y)

ans = 0
for i in range(N):
    ans += abs(X[i] - rx) + abs(Y[i] - ry)
print(int(ans))