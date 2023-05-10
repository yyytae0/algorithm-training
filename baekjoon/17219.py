from sys import stdin, stdout


n, m = map(int, stdin.readline().split())
dct = dict()
for i in range(n):
    a, b = map(str, stdin.readline().split())
    dct[a] = b

for i in range(m):
    a = stdin.readline().strip()
    stdout.write(dct[a] + '\n')