from collections import deque


def play():
    now = [1, 1, 0]
    d = [0, 1]
    cnt = 0
    t = 0
    tail = deque()
    for i in move:
        for j in range(int(i[0])-cnt):
            cnt += 1
            now = [now[0] + d[0], now[1] + d[1], now[2]]
            if 1 <= now[0] <= n and 1 <= now[1] <= n and [now[0], now[1]] not in tail:
                if lst[now[0]][now[1]]:
                    t += 1
                    tail.append([now[0] - d[0], now[1] - d[1]])
                else:
                    if t:
                        tail.popleft()
                        tail.append([now[0] - d[0], now[1] - d[1]])
            else:
                return cnt

        if i[1] == 'D':
            if now[2] == 0:
                d = [1, 0]
                now[2] = 1
            elif now[2] == 1:
                d = [0, -1]
                now[2] = 2
            elif now[2] == 2:
                d = [-1, 0]
                now[2] = 3
            elif now[2] == 3:
                d = [1, 0]
                now[2] = 0
        elif i[1] == 'L':
            if now[2] == 0:
                d = [-1, 0]
                now[2] = 3
            elif now[2] == 1:
                d = [0, 1]
                now[2] = 0
            elif now[2] == 2:
                d = [1, 0]
                now[2] = 1
            elif now[2] == 3:
                d = [0, -1]
                now[2] = 2

    while True:
        cnt += 1
        now = [now[0] + d[0], now[1] + d[1], now[2]]
        if lst[now[0]][now[1]]:
            t += 1
            tail.append([now[0] - d[0], now[1] - d[1]])
        else:
            if t:
                tail.popleft()
                tail.append([now[0] - d[0], now[1] - d[1]])
        if 1 <= now[0] <= n and 1 <= now[1] <= n and [now[0], now[1]] not in tail:
            pass
        else:
            return cnt


n = int(input())
k = int(input())
lst = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(k):
    x, y = map(int, input().split())
    lst[x][y] = 1

l = int(input())
move = list(list(input().split()) for _ in range(l))
ans = play()
print(ans)
