n = int(input())
cnt = 0
for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                for e in range(0, 10):
                    for f in range(0, 10):
                        cnt += 1
                        if cnt == n:
                            print(str(a)+str(a)+str(b)+str(c)+str(d)+str(d)+str(e)+str(f)+str(e))
                            exit()