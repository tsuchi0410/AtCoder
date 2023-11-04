N, M = map(int, input().split())
lr = []
for i in range(M):
    a, b = map(int, input().split())
    lr.append([a, b])

# 区間の右端の数字が小さい順番になるように、昇順に並び替え
lr = sorted(lr, key=lambda x: x[1])
# 初期値
x = lr[0][1]

ans = 1
for i in range(M - 1):
    if lr[i + 1][0] < x:
        continue
    else:
        x = lr[i + 1][1]
        ans += 1
print(ans)