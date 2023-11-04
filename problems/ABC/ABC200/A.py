N = str(input())

if len(N) < 3:
    print("1")
    exit()

if len(N) < 4:
    if N[-1] == "0" and N[-2] == "0":
        print(N[0])
        exit()
    else:
        x = int(N[0])
        print(x+1)
        exit()

if len(N) < 5:
    if N[-1] == "0" and N[-2] == "0":
        print(N[0]+N[1])
        exit()
    else:
        x = N[0] + N[1]
        x = int(x)
        print(x+1)
        exit()