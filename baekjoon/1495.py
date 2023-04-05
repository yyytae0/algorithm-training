def check():
    for i in range(n):
        cnt = 0
        for j in range(m + 1):
            if dp[i][j]:
                cnt += 1
                for k in [-1, 1]:
                    nj = j + k * lst[i]
                    if 0 <= nj <= m:
                        dp[i + 1][nj] = 1
        if cnt == 0:
            return -1
    for i in range(m, -1, -1):
        if dp[-1][i]:
            return i
    return -1


n, s, m = map(int, input().split())
lst = list(map(int, input().split()))
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
dp[0][s] = 1
print(check())
