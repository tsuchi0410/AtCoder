N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A + B
C.sort()

# 集合型にすることで重複を除去し、小さい順にソートする
C2 = sorted(set(C))
# B の各要素が何番目の要素なのかを辞書型で管理する
D = { v: i for i, v in enumerate(C2) }

for i in range(N):
    print(D[A[i]] + 1, end=" ")

print()

for i in range(M):
    print(D[B[i]] + 1, end=" ")