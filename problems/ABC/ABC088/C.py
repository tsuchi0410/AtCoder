import sys

C1 = list(map(int,input().split()))
C2 = list(map(int,input().split()))
C3 = list(map(int,input().split()))


for i in range(101):
    a1 = i
    b1 = C1[0] - a1
    b2 = C1[1] - a1
    b3 = C1[2] - a1

    if C2[0] - b1 == C2[1] - b2 and C2[0] - b1 == C2[2] - b3:
        if C3[0] - b1 == C3[1] - b2 and C3[0] - b1 == C3[2] - b3:
            print("Yes")
            sys.exit()

print("No")