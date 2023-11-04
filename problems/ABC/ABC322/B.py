N, M = map(int, input().split())
S = input()
T = input()

if T[:N] == S and T[-N:] == S:
    print(0)
    exit()

if T[:N] == S and T[-N:] != S:
    print(1)
    exit()

if T[:N] != S and T[-N:] == S:
    print(2)
    exit()

print(3)