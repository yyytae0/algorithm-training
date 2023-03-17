n = int(input())
case = 1
while n:
    lst = list(list(map(int, input().split())) for _ in range(n))
    dp = [[0, 0, 0] for _ in range(n)]
    dp[0] = lst[0][:]
    dp[1][0] = lst[0][1]+lst[1][0]
    dp[1][1] = min(lst[0][1], dp[1][0], lst[0][1]+lst[0][2])+lst[1][1]
    dp[1][2] = min(lst[0][1], lst[0][1]+lst[0][2], dp[1][1])+lst[1][2]
    for i in range(2, n):
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + lst[i][0]
        dp[i][1] = min(min(dp[i-1]), dp[i][0]) + lst[i][1]
        dp[i][2] = min(min(dp[i-1][1], dp[i-1][2]), dp[i][1]) + lst[i][2]
    print(f'{case}. {dp[-1][1]}')
    n = int(input())
    case += 1
