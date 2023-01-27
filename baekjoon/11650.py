from sys import stdin

ip = int(input())
lst = list()
for i in range(ip):
    lst.append(list(map(int, stdin.readline().split())))

lst.sort()
for i in lst:
    print(*i)
