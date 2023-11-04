A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0

for x in range(A+1):
    for y in range(B+1):
        for z in range(C+1):
            if 500*x + 100*y + 50*z == X:
                ans += 1
     

print(ans) 
