ip = list(input())
ans = ['' for _ in range(len(ip))]

ip.sort()
cnt = 0
odd = False
for i in range(0, len(ip), 2):
    if i == len(ip) - 1 or odd:
        if ip[i] == ip[i-1]:
            ans[cnt] = ip[i]
            ans[-cnt - 1] = ip[i]
            cnt += 1
        else:
            ans[len(ip) // 2] = ip[i]

    else:
        if ip[i] == ip[i + 1]:
            ans[cnt] = ip[i]
            ans[-cnt - 1] = ip[i]
            cnt += 1

        else:
            ans[len(ip) // 2] = ip[i]
            odd = True

real_ans = "".join(ans)
if len(real_ans) != len(ans):
    print('I\'m Sorry Hansoo')

else:
    print(real_ans)
