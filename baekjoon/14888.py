def dfs(d, idx):
    global mx, mn
    if idx == n:
        if d > mx:
            mx = d
        if d < mn:
            mn = d
        return

    for i in range(4):
        if calc[i]:
            nd = d
            if i == 0:
                nd += lst[idx]
            elif i == 1:
                nd = d - lst[idx]
            elif i == 2:
                nd = d*lst[idx]
            else:
                nd = int(d/lst[idx])
            calc[i] -= 1
            dfs(nd, idx+1)
            calc[i] += 1


n = int(input())
lst = list(map(int, input().split()))
calc = list(map(int, input().split()))
mx, mn = -10**9, 10**9
dfs(lst[0], 1)
print(mx)
print(mn)