S = input()
NUM = 753
ans = 10 ** 18
for i in range(len(S) - 2):
    num = S[i] + S[i + 1] + S[i + 2]
    ans = min(ans, abs(NUM - (int(num))))
print(ans)