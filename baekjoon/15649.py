


lst = [1, 2, 3, 4, 5, 6, 7, 8]
n, m = map(int, input().split())
lst = lst[:n]
dummy = lst[:]

for i in lst:
    dummy.remove(i)
    while len(dummy) != 0:


print(lst)
