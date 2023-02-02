from collections import deque

def work(que, task, n):
    re = 0
    for i in task:
        if re == 0:
            if i == 'R':
                re = 1

            elif i == 'D':
                if n == 0:
                    return False
                que.popleft()
                n = n-1

        elif re == 1:
            if i == 'R':
                re = 0

            elif i == 'D':
                if n == 0:
                    return False
                que.pop()
                n = n-1

    if re == 1:
        que.reverse()
        return que

    elif re == 0:
        return que


ip = int(input())

for i in range(ip):
    task = list(input())
    n = int(input())
    if n == 0:
        dummy = input()
        pass

    else:
        que = deque(map(int, input()[1:-1].split(',')))
        print(work(que, task, n))



