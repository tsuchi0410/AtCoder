import numpy as np
import math

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))

ab = math.sqrt((B[0]-A[0])*(B[0]-A[0])+(B[1]-A[1])*(B[1]-A[1]))
bc = math.sqrt((C[0]-B[0])*(C[0]-B[0])+(C[1]-B[1])*(C[1]-B[1]))
cd = math.sqrt((D[0]-C[0])*(D[0]-C[0])+(D[1]-C[1])*(D[1]-C[1]))
da = math.sqrt((D[0]-A[0])*(D[0]-A[0])+(D[1]-A[1])*(D[1]-A[1]))

ca = math.sqrt((A[0]-C[0])*(A[0]-C[0])+(A[1]-C[1])*(A[1]-C[1]))
bd = math.sqrt((D[0]-B[0])*(D[0]-B[0])+(D[1]-B[1])*(D[1]-B[1]))


def intersect(p1, p2, p3, p4):
    tc1 = (p1[0] - p2[0]) * (p3[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p3[0])
    tc2 = (p1[0] - p2[0]) * (p4[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p4[0])
    td1 = (p3[0] - p4[0]) * (p1[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p1[0])
    td2 = (p3[0] - p4[0]) * (p2[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p2[0])
    return tc1*tc2<0 and td1*td2<0


ans = intersect(A,C,B,D)

if ans == True:
    print("Yes")
else:
    print("No")
    


