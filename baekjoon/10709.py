h, w = map(int, input().split())
lst = list(list(input()) for _ in range(h))
ans = [[-1 for _ in range(w)] for _ in range(h)]

for i in range(h):
    now = 0
    for j in range(w):
        if now:
            now += 1

        if lst[i][j] == 'c':
            ans[i][j] = 0
            now = 1
        else:
            if now:
                ans[i][j] = now-1

for i in ans:
    print(*i)
