N = int(input())
S = [input() for _ in range(N)]
ans = 10 ** 10
for t in range(10):
    cnt = 0
    st = set()
    for num in S:
        for k in range(10):
            if num[k] == str(t):
                tmp = k
                while True:
                    if tmp in st:
                        tmp += 10
                    else:
                        st.add(tmp)
                        break
        cnt = max(cnt, tmp)
    ans = min(ans, cnt)
print(ans)