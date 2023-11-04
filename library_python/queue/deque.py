from collections import deque

A = deque([1,"two",3,"four",5])

A.append(6)         # 右端に挿入        deque([1, 'two', 3, 'four', 5, 6])
A.appendleft("#")   # 左端に挿入        deque(['#', 1, 'two', 3, 'four', 5, 6])
A.pop()             # 右端を取り出し    deque(['#', 1, 'two', 3, 'four', 5])
A.popleft()         # 左端を取り出し    deque([1, 'two', 3, 'four', 5])
print(A[0])         # 左端を表示        1
print(A[-1])        # 右端を表示        5