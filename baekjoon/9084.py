ip = int(input())

for case in range(ip):
    n = int(input())
    lst = list(map(int, input().split()))
    m = int(input())
    dp = [0 for _ in range(m+1)]
    for i in lst:
        dp[i] = 1
    for i in range(1, m+1):
        cnt = 0
        for j in lst:
            if j >= i:
                break
            else:
                if dp[i-j]:
                    cnt += 1
                    dp[i] += dp[i-j]
        dp[i] -= cnt-1
    print(dp)
    print(dp[m])
