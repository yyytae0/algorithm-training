from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
lst = list()
dct = dict()
for i in range(1, n+1):
    name = stdin.readline()[:-1]
    lst.append(name)
    dct[name] = i

for i in range(m):
    task = stdin.readline()[:-1]
    if task.isdigit():
        stdout.write(lst[int(task)-1] + '\n')

    else:
        stdout.write(str(dct[task]) + '\n')
