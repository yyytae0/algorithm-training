from sys import stdin

n, m = map(int, stdin.readline().split())
lst = list()
for i in range(n):
    ip = stdin.readline().strip()
    lst.append(ip)

cnt = 0
for i in range(m):
    ip = stdin.readline().strip()
    if ip in lst:
        cnt += 1

print(cnt)
