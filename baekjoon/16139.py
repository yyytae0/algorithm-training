from sys import stdin, stdout

ip = stdin.readline()
n = int(stdin.readline())

for _ in range(n):
    a, i, j = stdin.readline().split()
    ans = ip[int(i):int(j)+1].count(a)
    stdout.write(str(ans) + '\n')
