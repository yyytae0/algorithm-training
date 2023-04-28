from collections import deque


def bfs():
    q = deque()
    q.append([n, 0])
    mx = 100000
    cnt = 0
    while q:
        v = q.popleft()
        for i in [v[0]+1, v[0]-1, v[0]*2]:
            nv = [i, v[1]+1]
            if nv[1] > mx:
                continue
            if 0 <= i < 150000 and not dp[i]:
                if i == m:
                    mx = nv[1]
                    cnt += 1
                else:
                    dp[i] = 1
                    q.append(nv)
    print(mx)
    print(cnt)


n, m = map(int, input().split())
dp = [0 for _ in range(150000)]
dp[n] = 1
if n == m:
    print(0)
    print(1)
else:
    bfs()

# 1 4 > 2 2
# 예외 처리하기(visit)
