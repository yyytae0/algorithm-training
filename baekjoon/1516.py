def check(a):
    mx = 0
    if ans[a]:
        return ans[a]
    for i in lst[a]:
        mx = max(mx, check(i))
    ans[a] = mx + dp[a]
    return ans[a]


n = int(input())
dp = [0 for _ in range(n+1)]
ans = [0 for _ in range(n+1)]
lst = [[] for _ in range(n+1)]

for i in range(1, n+1):
    dummy = list(map(int, input().split()))
    dp[i] = dummy[0]
    for j in range(1, n+1):
        if dummy[j] != -1:
            lst[i].append(dummy[j])
        else:
            break

for i in range(1, n+1):
    if not ans[i]:
        check(i)

for i in range(1, n+1):
    print(ans[i])

#
# 5
# 10 -1
# 20 1 -1
# 30 2 -1
# 40 3 5 -1
# 100 -1
# result
# 10
# 30
# 60
# 140
# 100
