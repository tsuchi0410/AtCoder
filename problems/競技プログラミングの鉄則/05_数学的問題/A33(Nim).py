N = int(input())
A = list(map(int, input().split()))
x = 0
for i in A:
    x ^= i
if x != 0:
    print("First")
else:
    print("Second")