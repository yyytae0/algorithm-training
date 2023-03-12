def work():
    global lst
    lst[-1] -= 1
    lst[0] += 1


for case in range(1, 11):
    n = int(input())
    lst = list(map(int, input().split()))
    dummy = 0

    for i in range(n):
        lst.sort()
        if lst[-1] - lst[0] == 0:
            dummy = 1
            ans = 0
            break

        elif lst[-1] - lst[0] == 1:
            dummy = 1
            ans = 1
            break
        work()

    if dummy == 1:
        print(f'#{case} {ans}')

    else:
        ans = abs(max(lst[-1], lst[-2]) - min(lst[0], lst[1]))
        print(f'#{case} {ans}')
