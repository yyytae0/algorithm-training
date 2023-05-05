n = int(input())
lst = list(map(int, input().split()))
stack = []
ans = [0 for _ in range(n)]
for i in range(n):
    d = lst[i]
    while stack:
        t = stack.pop()
        if t[0] >= d:
            ans[i] = t[1]+1
            stack.append(t)
            stack.append([d, i])
            break
    else:
        stack.append([d, i])

print(*ans)
