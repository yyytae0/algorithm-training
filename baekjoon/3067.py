ip = int(input())

for case in range(ip):
    n = int(input())
    lst = list(map(int, input().split()))
    m = int(input())
    dp = [[0 for _ in range(n)] for _ in range(m+1)]
    for i in range(n):
        dp[lst[i]][i] = 1
    for i in range(1, m+1):
        for j in range(n):
            if lst[j] > i:
                break
            dp[i][j] = max(sum(dp[i-lst[j]][j:]), dp[i][j])
    print(sum(dp[m]))
