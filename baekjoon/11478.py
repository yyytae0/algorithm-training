ip = input()
cnt = 1
ans = list()
while cnt <= len(ip):
    for i in range(len(ip)-cnt+1):
        ans.append(ip[i:i+cnt])
    cnt += 1

print(len(set(ans)))
