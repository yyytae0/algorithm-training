from sys import stdin, stdout


n, m = map(int, input().split())
lst = list(map(int, input().split()))
for i in range(1, n):
    lst[i] = lst[i-1] + lst[i]

for _ in range(m):
    i, j = map(int, stdin.readline().split())
    if i == 1:
        stdout.write(str(lst[j-1]) + '\n')

    else:
        stdout.write(str((lst[j-1] - lst[i-2])) + '\n')
