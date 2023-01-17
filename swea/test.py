a = [1, 2, 3, 5]
b = a[:]
b.append(6)
print(id(b))
# b = [2, 3, 5]

print(a)
print(b)
print(id(a))
print(id(b))
