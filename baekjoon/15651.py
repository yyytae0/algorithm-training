def dfs(n, m):
    global s
    global lst
    if len(s) == m:
        lst.append(s[:])
        return
    
    for i in range(1, n+1):
        s.append(i)
        dfs(n, m)
        s.pop()


n, m = map(int, input().split())
s = []
lst = []
dfs(n, m)

for i in lst:
    print(*i)
