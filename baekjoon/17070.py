from collections import deque


def bfs():
    q = deque()
    cnt = 0
    way = [[[1, 1, 1], [0, 1, 0]], [[1, 1, 1], [1, 0, 2], [0, 1, 0]], [[1, 1, 1], [1, 0, 2]]]
    q.append([0, 1, 0])
    while q:
        v = q.popleft()
        for i in way[v[2]]:
            new_v = [v[0] + i[0], v[1] + i[1], i[2]]
            n0 = new_v[0]
            n1 = new_v[1]
            if i[2] == 1:
                if n0 <= n - 1 and n1 <= n - 1 and not lst[n0][n1] and not lst[n0-1][n1] and not lst[n0][n1-1]:
                    q.append(new_v)
                    if [n0, n1] == [n - 1, n - 1]:
                        cnt += 1
            else:
                if n0 <= n - 1 and n1 <= n - 1 and not lst[n0][n1]:
                    q.append(new_v)
                    if [n0, n1] == [n - 1, n - 1]:
                        cnt += 1

    return cnt


n = int(input())
lst = list(list(map(int, input().split())) for _ in range(n))
ans = bfs()
print(ans)
