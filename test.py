N = int(input())
l = [1]
for i in range(1, N):
    l2 = l + [i + 1] + l
    l = l2

for i in range(len(l)):
    print(l[i], end = " ")
print()