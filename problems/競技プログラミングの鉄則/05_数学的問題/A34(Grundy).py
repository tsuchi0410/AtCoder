N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
grundy = [0] * (max(A) + 1)
for i in range(max(A) + 1):
    st = set()
    if i - X >= 0:
        st.add(grundy[i - X])
    if i - Y >= 0:
        st.add(grundy[i - Y])
    for j in range(0, 10000):
        if j in st:
            continue
        else:
            grundy[i] = j
            break

x = 0
for i in range(N):
    x ^= grundy[A[i]]
if x != 0:
    print("First")
else:
    print("Second")