n = int(input())
lst = list(map(int, input().split()))
lst.sort()
new = [0 for _ in range(n)]
dummy = 0
for i in range(n):
    if dummy == 0:
        new[idx] = lst.pop()
    else:
        new[idx] = lst.pop(0)
    dummy = 1 - dummy
print(new)
ans = 0
for i in range(0, n-1):
    ans += abs(new[i] - new[i+1])
print(ans)
