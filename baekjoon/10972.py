n = int(input())
lst = list(map(int, input().split()))
stack = list()
dummy = 0
ans = 0
for i in range(n-1, -1, -1):
    if lst[i] > dummy:
        d = lst.pop()
        stack.append(d)
        dummy = d
    else:
        d = lst.pop()
        for j in stack:
            if j > d:
                lst.append(j)
                stack.remove(j)
                break
        stack.append(d)
        stack.sort()
        ans = lst + stack
        break

if ans:
    print(*ans)
else:
    print(-1)
