from sys import stdin, stdout

ip = int(stdin.readline())
ans = list()

for i in range(ip):
    ans.append(int(stdin.readline()))

ans.sort()

for i in ans:
    stdout.write(str(i)+'\n')
