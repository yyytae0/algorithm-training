n, s, m = map(int, input().split())
lst = list(map(int, input().split()))
dp = [[0, 0] for _ in range(m+1)]
dp[s] = [1, 0]
for i in range(1, n+1):
    d = 0
    for j in range(m+1):
        if dp[j][0] == i:
            d = 1
            a = j + lst[i-1]
            b = j - lst[i-1]
            if 0 <= a <= m:
                if dp[a][0] == i:
                    dp[a][1] = 1
                else:
                    dp[a][0] = i+1
            if 0 <= b <= m:
                if dp[b][0] == i:
                    dp[b][1] = 1
                else:
                    dp[b][0] = i+1
            if dp[j][1]:
                dp[j][0] = i+1
                dp[j][1] = 0
    if not d:
        print(-1)
        break
else:
    for j in range(m, -1, -1):
        if dp[j][0] == n+1:
            print(j)
            break
