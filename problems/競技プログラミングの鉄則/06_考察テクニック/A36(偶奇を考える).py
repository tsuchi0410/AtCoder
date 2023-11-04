N, K = map(int,input().split())
print("Yes") if K % 2 == 0 and K >= 2 * N - 2 else print("No")