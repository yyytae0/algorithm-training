from sys import stdin, stdout

ip = int(stdin.readline())
cnt = [0] * 10001
lst = list()
for i in range(ip):
    n = int(stdin.readline())
    cnt[n] += 1
    if cnt[n] == 1:
        lst.append(n)

lst.sort()
for i in lst:
    for j in range(cnt[i]):
        stdout.write(str(i)+'\n')
