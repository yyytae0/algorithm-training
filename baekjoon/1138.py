ip = int(input())
lst = list(map(int, input().split()))
order = [i for i in range(ip)]
ans = [0 for i in range(ip)]

for i in range(ip):
    dummy = order.pop(lst[i])
    ans[dummy] = i + 1

print(*ans)
