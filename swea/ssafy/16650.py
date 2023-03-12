ip = int(input())
for case in range(1, ip+1):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    ans = [0, 0, 0]
    for i in range(n):
        a, b = map(int, input().split())
        if x1 < a < x2 and y1 < b < y2:
            ans[0] += 1
        elif x1 <= a <= x2 and y1 <= b <= y2:
            ans[1] += 1
        else:
            ans[2] += 1
    print(f'#{case}', *ans)

