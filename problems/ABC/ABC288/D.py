n, k = (int(x) for x in input().split())
a = list(map(int,input().split()))

s = [0]
for i in range(n):
    s.append(s[i] + a[i])

print(s)

# q = int(input())
# for i in range(q):
#     l, r = (int(x) for x in input().split())
#     l -= 1  
#     if li[l:r] == a[l:r]:
#         print("Yes")
#     else:
#         print("No")