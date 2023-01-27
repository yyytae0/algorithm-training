from sys import stdin

n, m = map(int, stdin.readline().split())
lst = list()
for i in range(m):
    lst.append(list(map(int, stdin.readline().split())))

print(lst)
while len(lst) != 0:
    dummy = set(lst.pop(0))
    for i in lst:
        if (i[0] in dummy) or (i[1] in dummy):
            dummy = dummy.union({i[0], i[1]})

