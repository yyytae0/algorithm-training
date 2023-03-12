def check():
    ans = 0
    way = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    for i in range(n):
        for j in range(m):
            d = lst[i][j]
            cnt = 0
            for k in way:
                if 0 <= i + k[0] <= n-1 and 0 <= j + k[1] <= m-1 and lst[i+k[0]][j+k[1]] < d:
                    cnt += 1
            if cnt >= 4:
                ans += 1
    return ans


ip = int(input())

for case in range(1, ip+1):
    n, m = map(int, input().split())
    lst = list(list(map(int, input().split())) for _ in range(n))
    print(f'#{case} {check()}')
