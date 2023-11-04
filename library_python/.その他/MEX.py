"""
長さ N の非負整数列 
A が与えられます。
A から K 要素を選んで順序を保ったまま抜き出した列を B としたとき、 
MEX(B) としてありえる最大値を求めてください。
"""

N, K = (int(x) for x in input().split())
A = list(map(int,input().split()))

A = set(A)
for i in range(K):
    if not i in A:
        print(i)
        exit()

print(K)