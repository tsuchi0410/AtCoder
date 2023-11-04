N = int(input())
L = []
S = 0
for i in range(N):
    A, B = map(int,input().split())
    L.append([A, B])
    S += A

L2 = []
for i in range(N):
    A, B = L[i]
    L2.append([2 * A + B, i])
L2.sort(reverse = True)

T = 0
for i in range(N):
    T += L[L2[i][1]][0] + L[L2[i][1]][1]
    S -= L[L2[i][1]][0]
    if T > S:
        print(i + 1)
        exit()
