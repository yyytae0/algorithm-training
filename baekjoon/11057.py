dummy = []
cnt = 0


def dfs(a, n):
    if n == 0:
        cnt += 1
        return

    for i in range(a, 10):
        dfs(i, n-1)


n = int(input())

