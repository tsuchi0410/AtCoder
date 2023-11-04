N = int(input())
A = list(map(int,input().split()))

A2 = sorted(A, reverse = True)

Alice = []
Bob = []
for i in range(N):
    if i % 2 == 0:
        Alice.append(A2[i])
    else:
        Bob.append(A2[i])

print(sum(Alice) - sum(Bob))
    