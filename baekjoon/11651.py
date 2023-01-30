from sys import stdin

ip = int(stdin.readline())
lst = list()
for i in range(ip):
    lst.append(list(map(int, stdin.readline().split())))

lst.sort(key=lambda x: (x[1], x[0]))

for i in lst:
    print(*i)
