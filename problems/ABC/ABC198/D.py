import itertools
S1 = list(input())
S2 = list(input())
S3 = list(input())
N1 = len(S1)
N2 = len(S2)
N3 = len(S3)

S = set(S1 + S2 + S3)
if len(S) > 10:
    print("UNSOLVABLE")
    exit()

S = list(S)
lst = list(itertools.permutations(list(range(10)), len(S)))
for tup in lst:
    dic = {}
    cnt = 0
    for i in tup:
        dic[S[cnt]] = i
        cnt += 1
    num1 = 0
    num2 = 0
    num3 = 0
    if dic[S1[0]] == 0 or dic[S2[0]] == 0 or dic[S3[0]] == 0:
        continue
    for i in S1:
        num1 *= 10
        num1 += dic[i]
    for i in S2:
        num2 *= 10
        num2 += dic[i]
    for i in S3:
        num3 *= 10
        num3 += dic[i]
    if num1 + num2 == num3:
        print(num1)
        print(num2)
        print(num3)
        exit()
print("UNSOLVABLE")