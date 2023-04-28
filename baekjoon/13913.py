from collections import deque


def bfs():
    q = deque()
    q.append([n, 0])
    while q:
        v = q.popleft()
        for i in [v[0]+1, v[0]-1, 2*v[0]]:
            nv = [i, v[1]+1]
            if 0 <= i < 150000 and dp[i] < 0:
                q.append(nv)
                dp[i] = v[0]
                if i == m:
                    return nv[1]


n, m = map(int, input().split())
if n == m:
    print(0)
    print(n)
else:
    dp = [-1 for _ in range(150000)]
    dp[n] = n
    print(bfs())
    now = m
    ans = deque()
    while now != dp[now]:
        ans.appendleft(now)
        now = dp[now]
    ans.appendleft(now)
    print(*ans)
