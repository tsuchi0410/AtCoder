s = input()

# s[0] ~ s[n] の部分文字列 % 2019
n = len(s)
cnt = [0] * 2019
cnt[0] = 1
num = 0
d = 1
s = s[::-1]
for i in range(n):
    num += int(s[i]) * d
    num %= 2019
    d *= 10
    d %= 2019
    cnt[num] += 1

ans = 0
for i in range(2019):
    ans += cnt[i] * (cnt[i] - 1) // 2 

print(ans)