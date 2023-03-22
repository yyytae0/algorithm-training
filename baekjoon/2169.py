n, m = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
for j in range(1, m):
    lst[0][j] += lst[0][j-1]

for i in range(1, n):
    ltor = lst[i][:]
    rtol = lst[i][:]
    ltor[0] += lst[i-1][0]
    rtol[-1] += lst[i-1][-1]
    for j in range(1, m):
        ltor[j] += max(ltor[j-1], lst[i-1][j])
    for j in range(m-2, -1, -1):
        rtol[j] += max(rtol[j+1], lst[i-1][j])

    for j in range(m):
        lst[i][j] = max(ltor[j], rtol[j])
print(lst[-1][-1])
