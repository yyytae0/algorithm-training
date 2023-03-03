def check(a, d):
    global ans
    if d == s:
        ans += 1

    for i in range(a+1, n):
        check(i, d+lst[i])


n, s = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
for i in range(n):
    check(i, lst[i])
print(ans)