ip = list(input())
ans = ['' for _ in range(len(ip))]

ip.sort()

for i in range(len(ip)):
    ans[i] = (ip[i])
