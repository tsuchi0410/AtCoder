from collections import Counter

# Counter クラスを使用
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
b = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6]
a_counter = Counter(a)
b_counter = Counter(b)
print(a_counter) #Counter({5: 5, 4: 4, 3: 3, 2: 2, 1: 1})
print(b_counter) #Counter({6: 6, 4: 4, 3: 3, 2: 2, 1: 1})


# 和集合と差集合の演算が可能
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
b = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6]
a_counter = Counter(a)
b_counter = Counter(b)
print(a_counter + b_counter) #Counter({4: 8, 3: 6, 6: 6, 5: 5, 2: 4, 1: 2})
print(a_counter - b_counter) #Counter({5: 5})


# Counterの内容をソート
a = ["A", "B", "B", "C", "C", "C", "D", "D", "D", "D", "E", "E", "E", "E", "E"]
a_counter = Counter(a)
#昇順ソート
a_counter_sorted = [(l, k) for k, l in sorted([(j, i) for i, j in a_counter.items()])]
print(a_counter_sorted) #[('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5)]
#降順ソート
a_counter_sorted = [(l, k) for k, l in sorted([(j, i) for i, j in a_counter.items()], reverse=True)]
print(a_counter_sorted) #[('E', 5), ('D', 4), ('C', 3), ('B', 2), ('A', 1)]