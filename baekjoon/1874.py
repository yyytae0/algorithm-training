from sys import stdin, stdout


def check(lst, n):
    global chk
    stack = [0]
    ans = ''
    for i in lst:
        while stack[-1] != i:
            if chk[-1] == n+1:
                return False
            stack.append(chk.pop())
            ans = ans + '+' + '\n'

        dummy = stack.pop()
        if dummy == 0:
            return False

        else:
            ans = ans + '-' + '\n'

    return ans


ip = int(stdin.readline())
lst = list()
chk = [_ for _ in range(ip+1, 0, -1)]
for i in range(ip):
    lst.append(int(stdin.readline()))

ans = check(lst, ip)
if ans:
    stdout.write(ans)

else:
    stdout.write('NO')
