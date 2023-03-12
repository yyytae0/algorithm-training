def dfs(s, g):
    stack = list()
    stack.append(s)
    now = s
    visit[s] = 1
    while stack:
        for i in range(1, v + 1):
            if lst[now][i] and not visit[i]:
                stack.append(now)
                visit[i] = 1
                now = i
                if i == g:
                    return 1
                break
        else:
            if stack:
                now = stack.pop()
            else:
                return 0
    return 0


ip = int(input())

for case in range(1, ip+1):
    v, e = map(int, input().split())
    lst = [[0 for _ in range(v+1)] for _ in range(v+1)]
    for i in range(e):
        a, b = map(int, input().split())
        lst[a][b] = 1
    s, g = map(int, input().split())
    visit = [0 for _ in range(v+1)]
    ans = dfs(s, g)
    print(f'#{case} {ans}')
