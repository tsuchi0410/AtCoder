N, P, Q = map(int, input().split())
D = list(map(int, input().split()))
D.sort()

ans = P

num = Q
num += min(D)

print(min(ans, num))