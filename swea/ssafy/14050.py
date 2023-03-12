def bfs():
    ans = [0, [s]]
    q = list()
    q.append([s, 0])
    visit[s] = 1
    while q:
        v = q[0]
        del q[0]
        for i in range(1, 101):
            if phone[v[0]][i] and not visit[i]:
                q.append([i, v[1]+1])
                visit[i] = 1
                if v[1]+1 > ans[0]:
                    ans = [v[1]+1, [i]]
                elif v[1]+1 == ans[0]:
                    ans[1].append(i)
    return ans[1]


for case in range(1, 11):
    n, s = map(int, input().split())
    lst = list(map(int, input().split()))
    phone = [[0 for _ in range(101)] for _ in range(101)]
    visit = [0 for _ in range(101)]
    cnt = 0
    a = 0
    for i in lst:
        if not cnt:
            a = i
        else:
            phone[a][i] = 1
        cnt = 1 - cnt
    ans = bfs()
    print(f'#{case}', max(ans))
