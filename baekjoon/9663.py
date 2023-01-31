def dfs(n):
    global lstx
    global lsty
    global cnt
    if len(lsty) == n:
        cnt += 1
        return

    for x in range(lstx[-1], n):
        if x not in lstx:
            lstx.append(x)

        for y in range(n):
            if y not in lsty:
                print(x, y)
                lsty.append(y)
                dfs(n)
                lsty.pop()
        lstx.pop()


lstx = [0]
lsty = []
cnt = 0
ip = int(input())
dfs(ip)
print(cnt)
