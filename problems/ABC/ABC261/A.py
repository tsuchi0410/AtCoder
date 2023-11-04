#N = int(input())
L = list(map(int,input().split()))
#X, Y, Z = (int(x) for x in input().split())


red = [0]*101
f = 0
for i in range(len(red)):
    if L[0] == i:
        f = 1
    
    if L[1] == i:
        f = 0
    
    if f == 1:
        red[i] = 1

blue = [0]*101
f = 0
for i in range(len(blue)):
    if L[2] == i:
        f = 1
    
    if L[3] == i:
        f = 0
    
    if f == 1:
        blue[i] = 1


ans = 0
for i in range(len(red)):
    if red[i] == 1 and blue[i] == 1:
        ans += 1


print(ans)
    
