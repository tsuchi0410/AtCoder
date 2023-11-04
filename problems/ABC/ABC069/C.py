N = int(input())
a = list(map(int,input().split()))

num4 = 0
num2 = 0
num = 0
for i in range(N):
    if a[i] % 4 == 0:
        num4 += 1
    elif a[i] % 2 == 0:
        num2 += 1
    else:
        num += 1

num2 %= 2
num += num2

if num4 >= num:
    print("Yes")
elif abs(num4 - num) <= 1:
    print("Yes")
else:
    print("No")
