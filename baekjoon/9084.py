ip = int(input())

for case in range(ip):
    n = int(input())
    lst = list(map(int, input().split()))
    m = int(input())
    dp = [[0 for _ in range(n)] for _ in range(m+1)]
    for idx, i in enumerate(lst):
        if i > m:
            break
        dp[i][idx] = 1
    for i in range(1, m+1):
        for idx, j in enumerate(lst):
            if j >= i:
                break
            else:
                for k in range(idx, n):
                    if dp[i - j][k]:
                        dp[i][idx] += dp[i - j][k]
    print(sum(dp[m]))
