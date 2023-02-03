lst = list()
total = 0
for i in range(5):
    dummy = int(input())
    lst.append(dummy)
    total += dummy

lst.sort()
print(total//5)
print(lst[2])
