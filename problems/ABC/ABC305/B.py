p, q = map(str,input().split())
l = [3,1,4,1,5,9]
l2 = ["A","B","C","D","E","F","G"]
num1 = l2.index(p)
num2 = l2.index(q)
if num1 > num2:
    num1,num2=num2,num1
ans = 0
f = False
for i in range(len(l)):
    if num1 == i:
        f = True
    if f == True:
        ans += l[i]
    if num2-1 == i:
        print(ans)
        break