ip = int(input())

for case in range(1, ip+1):
    n, m, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    dp = [0 for _ in range(11112)]
    for i in range(1, 11112):
        dp[i] = dp[i-1]
        if not i % m:
            dp[i] += k
    for idx, i in enumerate(lst):
        if dp[i] <= idx:
            print(f'#{case} Impossible')
            break
    else:
        print(f'#{case} Possible')
