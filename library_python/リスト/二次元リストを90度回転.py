A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

A = [list(row) for row in zip(*A[::-1])]
