N = int(input())
ans = 0
for i in range(N, 101):
    if i % 5 == 0:
        ans = i
        break

ans2 = 0
for i in range(N, -1, -1):
    if i % 5 == 0:
        ans2 = i
        break

num1 = ans - N
num2 = N - ans2
if num1 <= num2:
    print(ans)
else:
    print(ans2)