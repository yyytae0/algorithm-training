import sys

# sys.stdin = open('input.txt', 'r')


def cnt(i, j):  # 방향(상하좌우) 별로 감시할 수 있는 영역
    ci, cj = i, j
    lst = []
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 상하좌우
        cnt = 0
        for k in range(1, 8):
            ni, nj = ci + di * k, cj + dj * k
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == 0:
                    cnt += 1
                elif arr[ni][nj] == 6:
                    break
            else:
                break
        lst.append((cnt, di, dj))
    return lst


def chg(di, dj):  # 방향별로 감시표시하기
    for k in range(1, 8):
        ni, nj = i + di * k, j + dj * k
        if 0 <= ni < n and 0 <= nj < m:
            if arr[ni][nj] == 0:
                arr[ni][nj] = '#'
            elif arr[ni][nj] == 6:
                break
        else:
            break


def cctv(i, j):
    n = arr[i][j]
    if n == 5:
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            chg(di, dj)
    elif n == 4:
        chg(0, -1)
        chg(0, 1)
        find = cnt(i, j)
        if find[0][0] > find[1][0]:
            chg(find[0][1], find[0][2])
        else:
            chg(find[1][1], find[1][2])
    elif n == 3:
        find = cnt(i, j)
        if find[0][0] > find[1][0]:
            chg(find[0][1], find[0][2])
        else:
            chg(find[1][1], find[1][2])
        if find[2][0] > find[3][0]:
            chg(find[2][1], find[2][2])
        else:
            chg(find[3][1], find[3][2])

    elif n == 2:
        find = cnt(i, j)
        if find[0] + find[1] > find[2] + find[3]:
            chg(find[0][1], find[0][2])
            chg(find[1][1], find[1][2])
        else:
            chg(find[2][1], find[2][2])
            chg(find[3][1], find[3][2])
    elif n == 1:
        find = max(cnt(i, j))
        chg(find[1], find[2])


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0 and arr[i][j] != 6 and arr[i][j] != '#':
            cctv(i, j)
ans = 0
for lst in arr:
    ans += lst.count(0)
print(ans)
