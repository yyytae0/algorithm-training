def check(t, multi):
    for i in lst[t]:
        if lst[i]:
            check(i, lst[t][i] * multi)
        else:
            cnt[i] += lst[t][i] * multi


n = int(input())
m = int(input())
cnt = [0 for _ in range(n+1)]
lst = [{} for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    lst[a][b] = c
check(n, 1)
for i in range(1, n):
    if cnt[i]:
        print(i, cnt[i])
