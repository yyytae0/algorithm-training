from sys import stdin, stdout


n = int(stdin.readline())
lst = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)
m = int(input())
for i in range(m):
    a, b = map(int, stdin.readline().split())
    if a == 1:
        if len(lst[b]) > 1:
            stdout.write('yes\n')
        else:
            stdout.write('no\n')
    else:
        stdout.write('yes\n')