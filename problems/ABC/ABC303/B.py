N, M = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(M)]
ans = 0
for i in range(N):
    cnt = 0
    st = set()
    for j in range(M):
        for k in range(N):
            if a[j][k] == i + 1:
                if k != 0:
                    st.add(a[j][k - 1])
                if k != N - 1:
                    st.add(a[j][k + 1])
    
    ans += N - 1 - len(st)

print(ans // 2)