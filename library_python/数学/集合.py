"""
和集合
"""
s1 = {0, 1, 2}
s2 = {1, 2, 3}
s3 = {2, 3, 4}

print(s1 | s2)
# {0, 1, 2, 3}

print(s1.union(s2))
# {0, 1, 2, 3}


"""
差集合
"""
s1 = {0, 1, 2}
s2 = {1, 2, 3}
s3 = {2, 3, 4}

print(s1 - s2)
# {0}

print(s1.difference(s2))
# {0}

print(s1.difference(s2, s3))
# {0}



"""
積集合
"""
s1 = {0, 1, 2}
s2 = {1, 2, 3}
s3 = {2, 3, 4}

print(s1 & s2)
# {1, 2}

print(s1.intersection(s2))
# {1, 2}

print(s1.intersection(s2, s3))
# {2}


"""
対称差集合(XOR : どちらか一方だけに含まれる)
"""
s1 = {0, 1, 2}
s2 = {1, 2, 3}
s3 = {2, 3, 4}

print(s1 ^ s2)
# {0, 3}

print(s1.symmetric_difference(s2))
# {0, 3}


"""
部分集合判定
"""
s1 = {0, 1}
s2 = {0, 1, 2, 3}

print(s1 <= s2)
# True

print(s1.issubset(s2))
# True


"""
上位集合判定
"""
s1 = {0, 1}
s2 = {0, 1, 2, 3}

print(s2 >= s1)
# True

print(s2.issuperset(s1))
# True


"""
互いに素(共通する要素がないか)判定
"""
s1 = {0, 1}
s2 = {1, 2}
s3 = {2, 3}

print(s1.isdisjoint(s2))
# False

print(s1.isdisjoint(s3))
# True