import itertools
N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
c = [list(map(int, input().split())) for _ in range(N)]

dic = {}
for i in range(3):
    for j in range(C):
        dic[(i, j)] = 0

for i in range(C):
    for j in range(N):
        for k in range(N):
            dic[((j + 1 + k + 1) % 3, i)] += D[c[j][k] - 1][i]

ans = 10 ** 18
lst = list(itertools.permutations(list(range(C)), 3))
for i in lst:
    c1, c2, c3 = i
    num = dic[(0, c1)] + dic[(1, c2)] + dic[(2, c3)]
    ans = min(ans, num)
print(ans)
