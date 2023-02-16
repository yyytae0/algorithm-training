def qsort(a):
    if len(a) < 2:
        return a
    p = a.pop()
    left = list()
    right = list()
    for i in a:
        if i < p:
            left.append(i)
        else:
            right.append(i)

    return qsort(left) + [p] + qsort(right)


ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = qsort(lst)
    print(f'#{case} {ans[n//2]}')
