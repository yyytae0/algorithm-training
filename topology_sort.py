def topology():
    ans = []
    while stack:
        v = stack.pop()
        ans.append(v)
        for i in lst[v]:
            temp[i] -= 1
            if not temp[i]:
                stack.append(i)
    return ans


n, m = map(int, input().split())
lst = [[] for _ in range(n+1)]
temp = [0 for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    temp[b] += 1
stack = []
for i in range(1, n+1):
    if not temp[i]:
        stack.append(i)
ans = topology()
print(*ans)
