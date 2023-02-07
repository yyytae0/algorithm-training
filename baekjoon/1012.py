def bfs(a, b):
    way = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    queue = [[a, b]]
    visit[a][b] = 1
    while queue:
        v = queue[0]
        del queue[0]
        for i in way:
            new_v = [v[0] + i[0], v[1] + i[1]]
            if 0 <= new_v[0] <= lst[1]-1 and 0 <= new_v[1] <= lst[0]-1:
                if visit[new_v[0]][new_v[1]] == 0 and arr[new_v[0]][new_v[1]] == 1:
                    queue.append(new_v)
                    visit[new_v[0]][new_v[1]] = 1


ip = int(input())

for i in range(ip):
    lst = list(map(int, input().split()))
    arr = [[0 for _ in range(lst[0])] for _ in range(lst[1])]
    visit = [[0 for _ in range(lst[0])] for _ in range(lst[1])]
    for j in range(lst[2]):
        dummy = list(map(int, input().split()))
        arr[dummy[1]][dummy[0]] = 1

    cnt = 0
    for j in range(lst[1]):
        for k in range(lst[0]):
            if arr[j][k] == 1 and visit[j][k] == 0:
                bfs(j, k)
                cnt += 1

    print(cnt)

