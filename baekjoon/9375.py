import collections

t = int(input())
for i in range(t):
    cnt = collections.Counter()
    ip = int(input())
    total = 1
    for j in range(ip):
        name, part = input().split()
        cnt[part] += 1
    for j in cnt.values():
        total = total * (j+1)
    print(total - 1)
