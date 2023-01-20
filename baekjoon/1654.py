from sys import stdin

ip = list(map(int, stdin.readline().split()))
lst = []
for i in range(ip[0]):
    lst.append(int(stdin.readline()))

print(lst)
