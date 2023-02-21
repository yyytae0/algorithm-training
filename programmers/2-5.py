from collections import deque


def solution(x, y, n):
    if x == y:
        return 0
    dp = [0 for _ in range(y+1)]
    idx = x
    q = deque()
    q.append(idx)
    while q:
        v = q.popleft()
        for i in [v+n, v*2, v*3]:
            if i < y:
                if not dp[i]:
                    q.append(i)
                    dp[i] = dp[v] + 1
            elif i == y:
                return dp[v] + 1
            else:
                continue
    return -1