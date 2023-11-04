
#L = list(map(int,input().split()))
#X, Y, Z = (int(x) for x in input().split())

Y = int(input())

while(1):
    if Y % 4 == 2:
        print(Y)
        exit()
    else:
        for i in range(1, 4):
            Y += 1
            if Y % 4 == 2:
                print(Y)
                exit()