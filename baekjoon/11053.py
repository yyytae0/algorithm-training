ip = int(input())
lst = list(map(int, input().split()))

ans = [1 for i in range(ip)]
for i in range(len(lst)):
    for j in range(i):
        if lst[i] > lst[j] and ans[j] + 1 > ans[i]:
            ans[i] = ans[j] + 1

print(max(ans))
