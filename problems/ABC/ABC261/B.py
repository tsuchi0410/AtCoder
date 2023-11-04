import sys

N = int(input())
#A = list(map(int,input().split()))
#X, Y, Z = (int(x) for x in input().split())

A = []
for i in range(N):
     A.append(str(input()))



for i in range(N):
    for j in range(N):
        if A[i][j] == "W" and A[j][i] == "W":
            print("incorrect")
            sys.exit()
        if A[i][j] == "W" and A[j][i] == "D":
            print("incorrect")
            sys.exit()
        if A[i][j] == "W" and A[j][i] == "-":
            print("incorrect")
            sys.exit()

        if A[i][j] == "L" and A[j][i] == "L":
            print("incorrect")
            sys.exit()
        if A[i][j] == "L" and A[j][i] == "D":
            print("incorrect")
            sys.exit()
        if A[i][j] == "L" and A[j][i] == "-":
            print("incorrect")
            sys.exit()

        if A[i][j] == "D" and A[j][i] == "W":
            print("incorrect")
            sys.exit()
        if A[i][j] == "D" and A[j][i] == "L":
            print("incorrect")
            sys.exit()
        if A[i][j] == "D" and A[j][i] == "-":
            print("incorrect")
            sys.exit()
        
        if A[i][j] == "-" and A[j][i] == "W":
            print("incorrect")
            sys.exit()
        if A[i][j] == "-" and A[j][i] == "L":
            print("incorrect")
            sys.exit()
        if A[i][j] == "-" and A[j][i] == "D":
            print("incorrect")
            sys.exit()

print("correct")


            

