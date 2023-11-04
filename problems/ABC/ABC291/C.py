N = int(input())
S = input()

s = set()
now = [0, 0]
s.add(tuple(now))
for i in range(N):
    if S[i] == "R":
        now[0] += 1
        if tuple(now) in s:
            print("Yes")
            exit()
        s.add(tuple(now))
    elif S[i] == "L":
        now[0] -= 1
        if tuple(now) in s:
            print("Yes")
            exit()
        s.add(tuple(now))
    elif S[i] == "U":
        now[1] += 1
        if tuple(now) in s:
            print("Yes")
            exit()
        s.add(tuple(now))
    else:
        now[1] -= 1
        if tuple(now) in s:
            print("Yes")
            exit()
        s.add(tuple(now))

print("No")
