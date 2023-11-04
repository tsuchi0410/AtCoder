N, K = (int(x) for x in input().split())
R, S, P = (int(x) for x in input().split())
T = input()

def result(str):
    if str == "r":
        return P
    elif str == "s":
        return R
    else:
        return S

ans = 0
flag = [True] * N
for i in range(N):
    if i + K < N:
        if T[i] == T[i + K]:
            if flag[i] == True:
                ans += result(T[i])
                flag[i + K] = False
        else:
            if flag[i] == True:
                ans += result(T[i])
    else:
        if flag[i] == True:
            ans += result(T[i])

print(ans)
