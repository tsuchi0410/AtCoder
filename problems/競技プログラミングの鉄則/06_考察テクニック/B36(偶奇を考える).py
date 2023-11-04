N, K = map(int,input().split())
S = input()
print("Yes") if S.count("1") % 2 == K % 2 else print("No")