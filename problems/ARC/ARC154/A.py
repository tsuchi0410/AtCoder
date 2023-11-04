n = int(input())
a = input()
b = input()

a2 = ""
b2 = ""
for i in range(n):
    if a[i] < b[i]:
        a2 += a[i]
        b2 += b[i]
    else:
        a2 += b[i]
        b2 += a[i]

print(int(a2) * int(b2) % 998244353)
