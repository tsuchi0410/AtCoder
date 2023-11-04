# for i in range(1 << n):

#     for j in range(n):
#         if (i >> j) & 1 == 1:
            
#             # True

# ビット列挙
NUM = 0
for i in range(2 ** NUM):
    l = [i >> j & 1 for j in range(NUM)]
    for j in range(len(l)):
        if l[j] == 1:
            