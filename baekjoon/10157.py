m, n = map(int, input().split())
k = int(input())
lst = [[0 for _ in range(m)] for _ in range(n)]
now = [0, 0]
way = [[1, 0], [0, 1], [-1, 0], [0, -1]]
d = 0
idx = 1
lst[now[0]][now[1]] = idx
if k == 1:
    print(now[1]+1, now[0]+1)
elif k > n*m:
    print(0)
else:
    while True:
        idx += 1
        new = [now[0] + way[d][0], now[1] + way[d][1]]
        if 0 <= new[0] < n and 0 <= new[1] < m and not lst[new[0]][new[1]]:
            now = [new[0], new[1]]
            lst[now[0]][now[1]] = idx
        else:
            d = (d + 1) % 4
            new = [now[0] + way[d][0], now[1] + way[d][1]]
            if 0 <= new[0] < n and 0 <= new[1] < m and not lst[new[0]][new[1]]:
                now = [new[0], new[1]]
                lst[now[0]][now[1]] = idx
            else:
                print(0)
                break
        if idx == k:
            print(now[1] + 1, now[0] + 1)
            break
