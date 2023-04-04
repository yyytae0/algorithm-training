n, m = map(int, input().split())
lst = [[0 for _ in range(m+1)]] + list(([0]+list(map(int, input()))) for _ in range(n))
mx = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if lst[i][j]:
            lst[i][j] = min(lst[i-1][j], lst[i][j-1], lst[i-1][j-1]) + 1
            if lst[i][j] > mx:
                mx = lst[i][j]
for i in lst:
    print(*i)
print(mx**2)
