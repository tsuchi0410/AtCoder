D = int(input())
N = int(input())
l = [0] * (D + 1)
for i in range(N):
    L, R = map(int, input().split())
    L -= 1
    l[L] += 1
    l[R] -= 1

s = [0]
for i in range(D + 1):
    s.append(s[i] + l[i])

print(*s[1:(D + 1)], sep = "\n")