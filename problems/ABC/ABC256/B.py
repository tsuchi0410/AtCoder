N = int(input())
A = list(map(int,input().split()))

P = 0
l = [0] * 4

for i in A:
    l[0] = 1
    
    for j in reversed(range(0, 4)):
        if l[j] == 1:
            if j + i >= 4:
                P += 1
            else:
                l[j + i] += 1
            l[j] = 0

print(P) 
          

