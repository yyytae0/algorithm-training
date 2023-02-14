from collections import deque


def play():
    now = [1, 1, 0]  # 시작좌표, 바라보는방향(0: 오른쪽, 1:아래, 2:왼쪽, 3:위)
    d = [0, 1]       # 바라보는 방향에 따른 초당 이동좌표
    cnt = 0          # 시간 및 정답이 될 변수
    t = 0            # 꼬리 길이
    tail = deque()   # 꼬리가 있는 좌표
    for i in move:
        for j in range(int(i[0])-cnt):  # 현재시간부터 방향전환까지 반복
            cnt += 1
            now = [now[0] + d[0], now[1] + d[1], now[2]]
            if 1 <= now[0] <= n and 1 <= now[1] <= n and [now[0], now[1]] not in tail:
                if lst[now[0]][now[1]]:     # 사과먹으면 꼬리 증가
                    t += 1
                    tail.append([now[0] - d[0], now[1] - d[1]])
                    lst[now[0]][now[1]] = 0  # 먹은 사과 제거
                else:
                    if t:
                        tail.popleft()        # 처음꼬리제거, 마지막위치 꼬리 추가
                        tail.append([now[0] - d[0], now[1] - d[1]])
            else:
                return cnt   # 벽이나 꼬리에 맞으면 return

        # 방향 전환

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

    # 방향 전환이 끝나고 계속 직진하는 경우

    while True:
        cnt += 1
        now = [now[0] + d[0], now[1] + d[1], now[2]]
        if 1 <= now[0] <= n and 1 <= now[1] <= n and [now[0], now[1]] not in tail:
            if lst[now[0]][now[1]]:
                t += 1
                tail.append([now[0] - d[0], now[1] - d[1]])
                lst[now[0]][now[1]] = 0
            else:
                if t:
                    tail.popleft()
                    tail.append([now[0] - d[0], now[1] - d[1]])
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
