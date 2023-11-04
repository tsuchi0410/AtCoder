S = input()
N = len(S)
if N % 2 == 0:
    print(0)
    exit()

# dp = [[0] * (N + 1) for _ in range(N)]
# dp[0][0] = 1
# for i in range(N):
#     for j in range(N):
#         if dp[i][j] >= 1:
#             if S[i] == "(":


