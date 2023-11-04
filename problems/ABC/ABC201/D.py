H, W = map(int, input().split())
A = [input() for _ in range(H)]

dp = [[10**18] * W for _ in range(H)]
dp[H - 1][W - 1] = 0
for i in range(H - 1, -1, -1):
    for j in range(W - 1, -1, -1):
        if i == H - 1 and j == W - 1:
            continue
        # Takahashi
        if (i + j) % 2 == 0:
            if i + 1 < H:
                if A[i + 1][j] == "+":
                    fi = 1
                else:
                    fi = -1
            if j + 1 < W:
                if A[i][j + 1] == "+":
                    fj = 1
                else:
                    fj = -1

            if i == H - 1:
                dp[i][j] = dp[i][j + 1] + fj
            elif j == W - 1:
                dp[i][j] = dp[i + 1][j] + fi
            else:
                dp[i][j] = max(dp[i + 1][j] + fi, dp[i][j + 1] + fj)

        
        # Aoki
        else:
            if i + 1 < H:
                if A[i + 1][j] == "-":
                    fi = 1
                else:
                    fi = -1
            if j + 1 < W:
                if A[i][j + 1] == "-":
                    fj = 1
                else:
                    fj = -1

            if i == H - 1:
                dp[i][j] = dp[i][j + 1] + fj
            elif j == W - 1:
                dp[i][j] = dp[i + 1][j] + fi
            else:
                dp[i][j] = min(dp[i + 1][j] + fi, dp[i][j + 1] + fj)

ans = dp[0][0]
if ans == 0:
    print("Draw")
elif ans > 0:
    print("Takahashi")
else:
    print("Aoki")