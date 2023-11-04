N = list(input())

if len(N) == 1:
    print("Yes")
    exit()

f = True
for i in range(len(N) - 1):
    if int(N[i]) <= int(N[i + 1]):
        f = False

if f == True:
    print("Yes")
else:
    print("No")