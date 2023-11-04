A, B = map(int,input().split())
cnt = 0
while True:
    if A > B:
        A = A - B
    else:
        B = B - A
    cnt += 1
    if A == B:
        print(cnt)
        exit()
