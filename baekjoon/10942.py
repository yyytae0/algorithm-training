from sys import stdin, stdout


n = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
dp = [[0 for _ in range(n)] for _ in range(n)]
# 홀수개의 팰린드롬의 경우
for i in range(n):
    dp[i][i] = 1
    for j in range(1, n):
        if 0 <= i+j < n and 0 <= i-j < n and lst[i+j] == lst[i-j]:
            dp[i-j][i+j] = 1
        else:
            break
# 짝수개의 팬린드롬의 경우
for i in range(n-1):
    a, b = lst[i], lst[i+1]
    if a == b:
        dp[i][i+1] = 1
        for j in range(1, n):
            if 0 <= i-j < n and 0 <= i+j+1 < n and lst[i-j] == lst[i+j+1]:
                dp[i-j][i+j+1] = 1
            else:
                break

m = int(stdin.readline())
for i in range(m):
    a, b = map(int, stdin.readline().split())
    stdout.write(str(dp[a-1][b-1])+'\n')
