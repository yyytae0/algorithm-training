def check(a, cnt):
    global ans
    if cnt == n//2:
        dummy = comp()
        if dummy < ans:
            ans = dummy
        return

    for i in range(a+1, n):
        food[i] = 1
        check(i, cnt+1)
        food[i] = 0


def comp():
    food_a = []
    food_b = []
    for i in range(n):
        if food[i]:
            food_a.append(i)
        else:
            food_b.append(i)
    return abs(calc(food_a) - calc(food_b))


def calc(arr):
    sm = 0
    for i in range(n//2):
        for j in range(i+1, n//2):
            sm += lst[arr[i]][arr[j]]
    return sm


ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = list(list(map(int, input().split())) for _ in range(n))
    food = [0 for _ in range(n)]
    ans = 10**6
    for i in range(n):
        for j in range(i, n):
            d = lst[i][j] + lst[j][i]
            lst[i][j], lst[j][i] = d, d
    check(-1, 0)
    print(f'#{case} {ans}')
