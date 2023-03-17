from sys import setrecursionlimit


def dfs(now, s, energy):
    global ans
    if now == n-1:
        if energy < ans:
            ans = energy
        return
    ns = (s+1) % 3
    for i in range(now+1, n):
        if a[i] == step[ns]:
            dfs(i, ns, energy+(i-now)**2)


setrecursionlimit(10**6)
n = int(input())
a = input()
step = ['B', 'O', 'J']
dct = {'B': 0, 'O': 1, 'J': 2}
ans = 10**6
dfs(0, dct[a[0]], 0)
if ans == 10**6:
    print(-1)
else:
    print(ans)