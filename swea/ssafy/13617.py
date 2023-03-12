ip = int(input())

for i in range(1, ip+1):
    n, q = map(int, input().split())
    ans = [0 for _ in range(n)]
    for j in range(1, q+1):
        start, last = map(int, input().split())
        for k in range(start-1, last):
            ans[k] = j

    print(f'#{i}', *ans)
