N, M = map(int, input().split())
a = list(map(int,input().split()))

stack = []
l = list(range(N))
for i in range(M):
    a[i] -= 1

ans = []
a_i = 0
i = 0
while True:
    if a[a_i] == i:
        stack.append(l[i + 1])
        a_i += 1
        i += 1
    else:
        stack = reversed(stack)
        ans += stack
        stack = []
        idx += 1

print(ans)