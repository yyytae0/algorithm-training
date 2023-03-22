def check():
    dp = [[0 for _ in range(n-m+2)] for _ in range(n)]
    for i in range(n):
        mx = 0
        for j in range(n-m+1):
            mxd = 0
            d = lst[i][j:j+m]
            for k in chk_lst:
                chk = 0
                sm = 0
                for kk in k:
                    sm += d[kk]
                    chk += d[kk]**2
                    if sm > c:
                        break
                else:
                    if chk > mxd:
                        mxd = chk
            dp[i][j] = mxd
            if mxd > mx:
                mx = mxd
        dp[i][-1] = mx
    return dp


def make_chk(a):
    for i in range(a+1, m):
        dummy.append(i)
        chk_lst.append(dummy[:])
        make_chk(i)
        dummy.pop()


ip = int(input())

for case in range(1, ip+1):
    n, m, c = map(int, input().split())
    lst = list(list(map(int, input().split())) for _ in range(n))
    chk_lst = []
    dummy = []
    make_chk(-1)
    dp = check()
    for i in range(n):
        dummy.append(dp[i][-1])
    dummy.sort()
    mx = dummy[-1] + dummy[-2]
    if n >= 2*m:
        for i in range(n):
            for j in range(n-2*m+1):
                for k in range(j+m, n-m+1):
                    if dp[i][j] + dp[i][k] > mx:
                        mx = dp[i][j] + dp[i][k]
    print(f'#{case} {mx}')
