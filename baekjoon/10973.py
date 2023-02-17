n = int(input())
lst = list(map(int, input().split()))
dummy = n+1
stack = list()
ans = 0
for i in range(n-1, -1, -1):
    if lst[i] < dummy:
        dummy = lst[i]
        stack.append(lst.pop())
    else:
        for j in stack:
            if j < lst[i]:
                stack.remove(j)
                stack.append(lst.pop())
                stack.sort(reverse=True)
                ans = lst + [j] + stack
                break
        break
if ans:
    print(*ans)
else:
    print(-1)
