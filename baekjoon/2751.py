from sys import stdin

ip = int(stdin.readline())
ans = [0]*ip

for i in range(ip):
    ans[i] = int(stdin.readline())

ans.sort()
s = ''

for i in ans:
    s += (str(i) + '\n')

print(s)
