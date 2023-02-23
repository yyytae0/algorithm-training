ip = int(input())

for _ in range(ip):
    n = int(input())
    total = sum(list(map(int, input().split())))
    ans = 1
    while n >= total:
        total = total * 4
        ans += 1
    print(ans)
