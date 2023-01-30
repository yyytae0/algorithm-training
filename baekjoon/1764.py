from sys import stdin, stdout
import collections

n, m = map(int, stdin.readline().split())
cnt = collections.Counter()
for i in range(n):
    cnt[stdin.readline()] += 1

for i in range(m):
    cnt[stdin.readline()] += 1

lst = list()
for i in cnt:
    if cnt[i] == 2:
        lst.append(i)

lst.sort()
print(len(lst))
for i in lst:
    stdout.write(i)
