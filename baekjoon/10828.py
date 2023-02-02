from sys import stdin, stdout


def stack(lst):
    global ans, cnt
    if lst[0] == 'push':
        ans.append(lst[1])
        cnt += 1
        return

    elif lst[0] == 'pop':
        if ans:
            cnt -= 1
            return ans.pop()

        else:
            return -1

    elif lst[0] == 'size':
        return cnt

    elif lst[0] == 'empty':
        if ans:
            return 0

        else:
            return 1

    elif lst[0] == 'top':
        if ans:
            return ans[-1]

        else:
            return -1


ip = int(stdin.readline())
ans = list()
cnt = 0
for i in range(ip):
    task = list(stdin.readline().split())
    re = stack(task)
    if re is not None:
        stdout.write(str(re) + '\n')
