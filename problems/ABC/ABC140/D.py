from itertools import*
import copy

N, K = map(int, input().split())
S = input()
S = [[k, len(list(v))] for k, v in groupby(S)]

ans_L = 0
ans_R = 0
# L
L_list = copy.deepcopy(S)
LK = K
for i in range(len(L_list)):
    if LK > 0:
        if S[i][0] == "R":
            L_list[i][0] = "L"
            LK -= 1
    else:
        break
L_list2 = []
for i in L_list:
    buf = i[0] * i[1]
    L_list2.append(buf)
L_list2 = "".join(L_list2)
for i in range(N - 1):
    if L_list2[i] == L_list2[i + 1]:
        ans_L += 1

# R
R_list = copy.deepcopy(S)
RK = K
for i in range(len(R_list)):
    if RK > 0:
        if S[i][0] == "L":
            R_list[i][0] = "R"
            RK -= 1
    else:
        break

R_list2 = []
for i in R_list:
    buf = i[0] * i[1]
    R_list2.append(buf)
R_list2 = "".join(R_list2)
for i in range(N - 1):
    if R_list2[i] == R_list2[i + 1]:
        ans_R += 1

print(max(ans_L, ans_R))