def dfs(n, m):
    global s
    global lst
    if len(s) == m+1:
        lst.append(s[1:])
        return

    for i in range(s[-1], n+1):
        if i not in s:
            s.append(i)
            dfs(n, m)
            s.pop()


s = [0]
lst = []
n, m = map(int, input().split())
dfs(n, m)

for i in lst:
    print(*i)
