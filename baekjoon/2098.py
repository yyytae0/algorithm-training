def dfs(x, visited):
    if visited == (1 << n) - 1:
        if lst[x][0]:
            return lst[x][0]
        return const

    if dp[x][visited] != const:
        return dp[x][visited]

    for i in range(1, n):
        if not lst[x][i]:
            continue
        if visited & (1 << i):
            continue
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + lst[x][i])
    return dp[x][visited]


n = int(input())
lst = list(list(map(int, input().split())) for _ in range(n))
const = int(1e9)
dp = [[const]*(1 << n) for _ in range(n)]
print(dfs(0, 1))
