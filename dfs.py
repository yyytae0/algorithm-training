def dfs(n, m):
    global s
    global li
    if len(s) == m:
        li.append(s[:])
        return

    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs(n, m)
            s.pop()


n, m = list(map(int, input().split()))
s = []
li = []

dfs(n, m)
for i in li:
    print(*i)