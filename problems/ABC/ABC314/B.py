N = int(input())

L = []

for i in range(N):
    C = int(input())
    A = list(map(int, input().split()))
    L.append(set(A))

X = int(input())

ans = []
ok = float("inf")
for i in range(N):
    if X in L[i]:
        ans.append([len(L[i]), i + 1])
        ok = min(ok, len(L[i]))
ans.sort()

ans2 = []
for i in range(len(ans)):
    if ans[i][0] == ok:
        ans2.append(ans[i][1])

ans2.sort()
print(len(ans2))
print(*ans2)