sx, sy, tx, ty = map(int,input().split())
x = tx - sx
y = ty - sy
ans = ""
ans += "U" * y
ans += "R" * x
ans += "D" * y
ans += "L" * x
ans += "L"
ans += "U" * (y + 1)
ans += "R" * (x + 1)
ans += "D"
ans += "R"
ans += "D" * (y + 1)
ans += "L" * (x + 1)
ans += "U"
print(ans)