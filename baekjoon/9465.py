def check():
    for i in range(2, n+1):
        lst[0][i] = max(lst[1][i-1], lst[1][i-2]) + lst[0][i]
        lst[1][i] = max(lst[0][i-1], lst[0][i-2]) + lst[1][i]

    return max(lst[0][n], lst[1][n])


ip = int(input())

for _ in range(ip):
    n = int(input())
    lst = list(([0] + list(map(int, input().split()))) for _ in range(2))
    ans = check()
    print(ans)
