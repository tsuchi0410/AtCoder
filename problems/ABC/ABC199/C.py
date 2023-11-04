N = int(input())
S = input()
Q = int(input())

S1 = list(S)
S2 = S[N:]+S[:N]
S2 = list(S2)

# print(S1)
# print(S2)

cnt = 0
for i in range(Q):
    T,A,B = (int(x) for x in input().split())
    A -= 1
    B -= 1

    if cnt % 2 == 0 and T == 1:
        S1[A],S1[B] = S1[B],S1[A]
        S2[A-N],S2[B-N] = S2[B-N],S2[A-N]
    
    if cnt % 2 == 1 and T == 1:
        S2[A],S2[B] = S2[B],S2[A]
        S1[A-N],S1[B-N] = S1[B-N],S1[A-N]

    if T == 2:
        cnt += 1

if cnt % 2 == 0:
    print(''.join(S1))
else:
    print(''.join(S2))