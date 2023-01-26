from sys import stdin

ip = int(stdin.readline())
lst = list()

for i in range(ip):
    a, b, c, d, e, f = map(int, stdin.readline().split())
    lst.append([(a, f), (c, e), (b, d)])

print(lst)

# for i in lst:
