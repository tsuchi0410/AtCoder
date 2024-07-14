from sortedcontainers import SortedSet, SortedList, SortedDict

S = SortedList([5,4,1,2,3])

S.add(10)

S.discard(1)

S.count()

S.index()

# min max は O(N)
