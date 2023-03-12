def check(a):
    global ans
    for i in dct[a]:
        ans.append(i)
        check(i)


ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = list(map(int, input().split()))
    dct = dict()
    ans = [1]
    for i in range(1, n + 1):
        dct[i] = []
    idx = 0
    for i in range(len(lst) // 2):
        dct[lst[idx]].append(lst[idx + 1])
        idx += 2
    check(1)
    print(f'#{case}', *ans)
