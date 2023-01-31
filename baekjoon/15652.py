def dfs(n, m):
    global s
    global lst
    if len(s) == m+1:
        lst.append(s[1:])
        return

    for i in range(s[-1], n+1):
        s.append(i)
        dfs(n, m)
        s.pop()


n, m = map(int, input().split())
s = [1]
lst = []
dfs(n, m)

for i in lst:
    print(*i)