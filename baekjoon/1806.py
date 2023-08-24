n, m = map(int, input().split())
lst = [0] + list(map(int, input().split()))
ans = 1000000


def find():
    for i in range(2, n + 1):
        for j in range(n + 1 - i):
            if lst[j + i] - lst[j] >= m:
                return i


for i in range(1, n+1):
    if lst[i] >= m:
        ans = 1
        break
    lst[i] += lst[i-1]
if ans != 1:
    if lst[n] < m:
        ans = 0
    elif lst[n] == m:
        ans = n
    else:
        ans = find()
print(ans)
