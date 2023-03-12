def dfs():
    stack = list()
    a = 0
    visit[a] = 1
    while True:
        for i in [mp1[a], mp2[a]]:
            if i and not visit[i]:
                stack.append(i)
                visit[i] = 1
                a = i
                if i == 99:
                    return 1
                break
        else:
            if stack:
                a = stack.pop()
            else:
                return 0


for case in range(1, 11):
    c, n = map(int, input().split())
    lst = list(map(int, input().split()))
    mp1 = [0 for _ in range(100)]
    mp2 = [0 for _ in range(100)]
    for i in range(n):
        s = lst[2*i]
        g = lst[2*i+1]
        if mp1[s]:
            mp2[s] = g
        else:
            mp1[s] = g
    visit = [0 for _ in range(100)]
    ans = dfs()
    print(f'#{case} {ans}')
