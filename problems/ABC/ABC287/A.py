
n = int(input())
s = []
for i in range(n):
    s.append(input())

if s.count("For") > s.count("Against"):
    print("Yes")
else:
    print("No")