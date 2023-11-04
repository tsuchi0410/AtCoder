N = int(input())
T = []
for i in range(N):
    T.append(list(map(int,input().split())))

for i in range(N):
    # odd
    if T[i][0] % 2 == 1 and (T[i][1] + T[i][2]) % 2 == 1:
        if T[i][1] + T[i][2] > T[i][0]:
            print("No")
            exit()
    # even
    elif T[i][0] % 2 == 0 and (T[i][1] + T[i][2]) % 2 == 0:
        if T[i][1] + T[i][2] > T[i][0]:
            print("No")
            exit()
    else:
        print("No")
        exit()

    if i > 0:
        if abs(T[i-1][0] - T[i][0]) < abs((T[i-1][1]+T[i-1][2]) - (T[i][1] + T[i][2])):
            print("No")
            exit()

print("Yes")

