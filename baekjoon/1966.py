from collections import deque

ip = int(input())

for i in range(ip):
    n, idx = map(int, input().split())
    lst = list(map(int, input().split()))
    que = deque(lst)
    target = que[idx]
    cnt = 0
    lst.sort()
    while True:
        dummy = que.popleft()
        if dummy == lst[-1]:
            cnt += 1
            if idx == 0:
                break
            lst.pop()
            idx -= 1

        else:
            que.append(dummy)
            if idx == 0:
                idx = len(que) - 1

            else:
                idx -= 1

    print(cnt)
