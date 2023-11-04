N = int(input())
A = []
for _ in range(N):
    C = int(input())
    a = list(map(int, input().split()))
    A.append(set(a))
X = int(input())
ans = [float("inf"), []]
for i, v in enumerate(A):
    if X in v:
        if ans[0] > len(v):
            ans = [len(v), [i + 1]]
        elif ans[0] == len(v):
            ans[1].append(i + 1)
        else:
            continue

if ans == [float("inf"), []]:
    print(0)
    print()
else:
    print(len(ans[1]))
    print(*ans[1])