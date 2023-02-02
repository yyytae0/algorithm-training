n, k = map(int, input().split())
lst = list()
for i in range(1, n+1):
    lst.append(i)

idx = k-1
ans = list()
while True:
    ans.append(lst.pop(idx))
    idx = idx + k - 1
    n = n - 1
    if n == 0:
        break

    while idx > n-1:
        idx = idx - n

print(f'<{str(ans)[1:-1]}>')
