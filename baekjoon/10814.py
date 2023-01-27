from sys import stdin

ip = int(input())
lst = list()
for i in range(ip):
    age, name = stdin.readline().split()
    lst.append([int(age), name])

lst.sort(key=lambda x: x[0])
for i in lst:
    print(*i)
