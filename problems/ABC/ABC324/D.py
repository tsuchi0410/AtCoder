N = int(input())
S = input()

dic = {}
for i in range(10):
    dic[str(i)] = 0

for i in S:
    dic[i] += 1

for i in range(10):
    x = str(i * i)

    dic2 = {}
    for i in range(10):
        dic2[str(i)] = 0

    for i in x:
        dic2[i] += 1

    print(dic - dic2)