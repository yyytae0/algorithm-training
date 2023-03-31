from collections import deque


def bfs():
    q = deque()
    q.append([0, 0])
    while q:
        v = q.popleft()
        idx = (v[1]+1) % 3
        for i in range(v[0]+1, n):
            if a[i] == step[idx]:
                d = dp[v[0]] + (i - v[0]) ** 2
                if dp[i] == 0:
                    dp[i] = d
                    q.append([i, idx])
                else:
                    if d < dp[i]:
                        dp[i] = d
                        q.append([i, idx])

    return dp[n-1]


n = int(input())
a = input()
step = ['B', 'O', 'J']
dp = [0 for _ in range(n)]
ans = bfs()
if ans == 0:
    print(-1)
else:
    print(ans)
