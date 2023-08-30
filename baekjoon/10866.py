from collections import deque
from sys import stdin, stdout

n = int(stdin.readline())
q = deque()
cnt = 0
for i in range(n):
    command = list(stdin.readline().split())
    c = command[0]
    if c == 'push_back':
        cnt += 1
        q.append(command[1])
    elif c == 'push_front':
        cnt += 1
        q.appendleft(command[1])
    elif c == 'front':
        if q:
            stdout.write(q[0] + '\n')
        else:
            stdout.write('-1' + '\n')
    elif c == 'back':
        if q:
            stdout.write(q[-1] + '\n')
        else:
            stdout.write('-1' + '\n')
    elif c == 'size':
        stdout.write(str(cnt) + '\n')
    elif c == 'empty':
        if cnt:
            stdout.write('0' + '\n')
        else:
            stdout.write('1' + '\n')
    elif c == 'pop_front':
        if q:
            d = q.popleft()
            stdout.write(str(d) + '\n')
            cnt -= 1
        else:
            stdout.write('-1' + '\n')
    elif c == 'pop_back':
        if q:
            d = q.pop()
            stdout.write(str(d) + '\n')
            cnt -= 1
        else:
            stdout.write('-1' + '\n')
