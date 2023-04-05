n, m = map(float, input().split())
while n:
    n = int(n)
    m = int(m*100+0.5)
    dp = [0 for _ in range(m+1)]
    for i in range(n):
        a, b = map(float, input().split())
        a = int(a)
        b = int(b*100+0.5)
        for j in range(b, m+1):
            dp[j] = max(dp[j-b] + a, dp[j])
    print(dp[m])
    n, m = map(float, input().split())
    if n <= 0:
        break
