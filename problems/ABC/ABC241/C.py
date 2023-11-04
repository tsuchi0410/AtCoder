N = int(input())
S = [list(input()) for _ in range(N)]

vec = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, -1), (-1, 1)]

for i in range(N):
    for j in range(N):
        for y, x in vec:
            if not 0 <= i + y * 5 < N:
                continue
            if not 0 <= j + x * 5 < N:
                continue
            cnt = 0
            for k in range(6):
                if S[i + y * k][j + x * k] == "#":
                    cnt += 1
            if cnt >= 4:
                print("Yes")
                exit()
print("No")