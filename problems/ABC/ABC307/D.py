from collections import deque
N = int(input())
S = input()
dq = deque([])
cnt = 0
for i in range(N):
    if S[i] == "(":
        cnt += 1
        dq.append("(")
    elif S[i] == ")":
        if cnt > 0:
            cnt -= 1
            while True:
                b = dq.pop()
                if b == "(":
                    break
        else:
            dq.append(")")
    else:
        dq.append(S[i])
print("".join(dq))