A = list(map(int,input().split()))


l = []
s = 'a'

for i in range(65, 91):
    s = s + chr(i)*A[0]



print(s[A[1]])