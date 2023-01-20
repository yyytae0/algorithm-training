def VPS(word):
    cnt = 0
    for i in word:
        if i == '(':
            cnt += 1

        else:
            if 0 >= cnt:
                return False

            else:
                cnt -= 1

    if cnt == 0:
        return True


ip = int(input())
ans = ''

for i in range(ip):
    a = input()
    if VPS(a):
        ans = ans + 'YES' + '\n'

    else:
        ans = ans + 'NO' + '\n'

print(ans)
