dp = [[0, 0] for _ in range(251)]
dp[0] = [1, 0]
dp[1] = [1, 0]
dp[2] = [1, 2]
for i in range(3, 251):
    dp[i][0] = sum(dp[i-1])
    dp[i][1] = sum(dp[i-2]) * 2

while True:
    try:
        n = int(input())
    except EOFError:
        break
    else:
        print(sum(dp[n]))
