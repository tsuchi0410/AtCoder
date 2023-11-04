N, X, Y = map(int, input().split())
P = [0] * N
T = [0] * N
for i in range(N - 1):
    P[i], T[i] = map(int, input().split())
Q = int(input())
q = list(int(input()) for _ in range(Q))

dic = {}
for i in range(900):
    cnt = i
    for j in range(N - 1):
        if cnt % P[j] == 0:
            mati = 0
        else:
            mati = P[j] - cnt % P[j]
        cnt += mati
        cnt += T[j]
    dic[i] = cnt - i

for i in range(Q):
    num = (X + q[i]) % 840
    print(q[i] + X + dic[num] + Y)
