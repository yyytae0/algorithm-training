def check(k):
    global ans
    for i in range(k//2-1+k%2, n):
        for j in range(k//2-1+k%2, n):
            cnt, money = bfs(i, j, k)
            if money > 0:
                if cnt > ans:
                    ans = cnt


def bfs(i, j, k):
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = list()
    visit = [[0 for _ in range(n)] for _ in range(n)]
    q.append([i, j, 1])
    cnt = lst[i][j]
    visit[i][j] = 1
    while q:
        v = q.pop(0)
        if v[2] + 1 > k:
            return cnt, ((cnt*m)-k*k-(k-1)*(k-1))
        for d in way:
            nv = [v[0] + d[0], v[1] + d[1], v[2] + 1]
            if 0 <= nv[0] < n and 0 <= nv[1] < n and not visit[nv[0]][nv[1]]:
                q.append(nv)
                visit[nv[0]][nv[1]] = 1
                if lst[nv[0]][nv[1]]:
                    cnt += 1
    return cnt, ((cnt * m) - k*k - (k - 1) * (k - 1))


ip = int(input())

for case in range(1, ip+1):
    ans = 0
    n, m = map(int, input().split())
    lst = list(list(map(int, input().split())) for _ in range(n))
    for i in range(1, n+1):
        check(i)
    print(f'#{case} {ans}')
