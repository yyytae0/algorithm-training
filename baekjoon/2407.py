n, m = map(int, input().split())
ans = 1
for i in range(n, 0, -1):
    if i <= max(n-m, m):
        if i <= min(n-m, m):
            ans = ans//i
    else:
        ans = ans * i

print(ans)
