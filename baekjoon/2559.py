n, k = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
total = 0
total_max = -10000000
for i in range(n):
    if i < k:
        total = total + lst[i]
        if i == k-1:
            total_max = total

    else:
        total = total + lst[i] - lst[cnt]
        cnt += 1
        if total > total_max:
            total_max = total

if total > total_max:
    total_max = total

print(total_max)
