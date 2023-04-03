from collections import deque


def bfs():
    q = deque()
    q.append(n)
    dp[n] = 1
    while q:
        v = q.popleft()
        for i in [v+1, v-1, v*2, v-10]:
            if 0 <= i < 2*m and not dp[i]:
                q.append(i)
                dp[i] = dp[v]+1
                if i == m:
                    return


ip = int(input())

for case in range(1, ip+1):
    n, m = map(int, input().split())
    dp = [0 for _ in range(2*m)]
    bfs()
    print(f'#{case} {dp[m]-1}')