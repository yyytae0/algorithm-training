from sys import stdin, stdout
from collections import deque


ip = int(stdin.readline())
que = deque()
cnt = 0
for i in range(ip):
    task = list(stdin.readline().split())
    if task[0] == 'push':
        que.append(task[1])
        cnt += 1

    elif task[0] == 'pop':
        if cnt == 0:
            stdout.write('-1\n')

        else:
            d = que.popleft()
            stdout.write(str(d) + '\n')
            cnt -= 1

    elif task[0] == 'size':
        stdout.write(str(cnt) + '\n')

    elif task[0] == 'empty':
        if cnt == 0:
            stdout.write('1\n')

        else:
            stdout.write('0\n')

    elif task[0] == 'front':
        if cnt == 0:
            stdout.write('-1\n')

        else:
            stdout.write(str(que[0]) + '\n')

    elif task[0] == 'back':
        if cnt == 0:
            stdout.write('-1\n')

        else:
            stdout.write(str(que[-1]) + '\n')
