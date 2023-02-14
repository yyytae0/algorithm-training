from collections import deque


a = deque()
a.append([1, 1])
a.append([1, 2])
print([1, 3] in a)
print([1, 2] in a)
