n, m = map(int, input().split())
r, c, d = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
way = [[-1, 0], [0, 1], [1, 0], [0, -1]]
now = [r, c]
ans = 0
while True:
    if lst[now[0]][now[1]] == 0:
        ans += 1
        lst[now[0]][now[1]] = 2
    for i in range(4):
        if lst[now[0]+way[d][0]][now[1]+way[d][1]] == 0:
            now = [now[0]+way[d][0], now[1]+way[d][1]]
            break
        d = (d + 3) % 4
    else:
        now = [now[0]-way[d][0], now[1]-way[d][1]]
        if lst[now[0]][now[1]] == 1:
            break
print(ans)
for i in lst:
    print(*i)
