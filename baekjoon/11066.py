ip = int(input())

for case in range(ip):
    n = int(input())
    lst = list(map(int, input().split()))
    subsum = [0 for _ in range(n+1)]
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        subsum[i] = subsum[i-1] + lst[i]

    for size in range(1, n):
        for s in range(n-1):
            e = s + size
            if e >= n:
                break

            dummy = float('inf')
            for d in range(s, e):
                dummy = min(dummy, dp[s][d]+dp[d+1][e]+subsum[e]-subsum[s-1])
            dp[s][e] = dummy

    print(dp[0][n-1])
