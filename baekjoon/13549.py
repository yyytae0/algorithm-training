from collections import deque


def bfs():
    global ans, flag
    q.append([n, 0])
    check([n, 0])
    while q:
        v = q.popleft()
        if flag:
            return ans
        for i in [v[0]-1, v[0]+1]:
            if 0 <= i < 2*mx and not visit[i]:
                check([i, v[1]+1])


def check(a):
    global ans, flag
    if k <= a[0] < 2*mx:
        dp[a[0]] = a[1]
        q.append([a[0], a[1]])
        visit[a[0]] = 1
        if a[0] == k:
            ans = a[1]
            flag = 1
            return
    else:
        for i in range(20):
            if a[0] * (2 ** i) < 2*mx and not visit[a[0] * (2 ** i)]:
                dp[a[0] * (2 ** i)] = a[1]
                q.append([a[0] * (2 ** i), a[1]])
                visit[a[0] * (2 ** i)] = 1
                if a[0] * (2 ** i) == k:
                    ans = a[1]
                    flag = 1
                    return
            else:
                break


n, k = map(int, input().split())
if n == k:
    print(0)
else:
    mx = max(n, k)
    dp = [0 for _ in range(2 * mx)]
    visit = [0 for _ in range(2 * mx)]
    q = deque()
    ans = 0
    flag = 0
    print(bfs())


