def bfs():
    global ans
    way = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    a = [0, 0]
    queue = [a]
    while queue:
        v = queue[0]
        del queue[0]
        for i in way:
            new_v = [v[0]+i[0], v[1]+i[1]]
            if 0 <= new_v[0] <= m-1 and 0 <= new_v[1] <= n-1:
                if visit[new_v[1]][new_v[0]] == 0 and lst[new_v[1]][new_v[0]] == 1:
                    queue.append(new_v)
                    visit[new_v[1]][new_v[0]] = 1
                    ans[new_v[1]][new_v[0]] = ans[v[1]][v[0]] + 1


n, m = map(int, input().split())
lst = list(list(map(int, input())) for _ in range(n))
visit = [[0 for _ in range(m)] for _ in range(n)]
ans = [[0 for _ in range(m)] for _ in range(n)]
ans[0][0] = 1
bfs()
print(ans[-1][-1])
