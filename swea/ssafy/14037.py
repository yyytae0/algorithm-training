def dfs(a):
    global ans
    if a == n-1:
        ans += 1
        return
    for i in range(n):
        if not y[i]:
            if check(a+1, i):
                y[i] = 1
                lst[a+1][i] = 1
                dfs(a+1)
                lst[a+1][i] = 0
                y[i] = 0


def check(a, b):
    for i in range(1, n):
        if (0 <= b-i < n and lst[a-i][b-i]) or (0 <= b+i < n and lst[a-i][b+i]):
            return False
    return True


ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = [[0 for _ in range(n)] for _ in range(n)]
    y = [0 for _ in range(n)]
    ans = 0
    for i in range(n):
        y[i] = 1
        lst[0][i] = 1
        dfs(0)
        y[i] = 0
        lst[0][i] = 0
    print(f'#{case} {ans}')

